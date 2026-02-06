from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re
import hashlib

# создаем кастомную модель пользователей
class User(AbstractUser):
    email = models.EmailField(unique=True,verbose_name="Email", error_messages={"unique":"Такое пользователь с email уже существует"})

    # поле с шифрованием(как пример в реальности тот же password берется с библиотеки)
    _encrypted_key = models.BinaryField(null=True,blank=True,verbose_name="Шифрование API ключа")

    ssh_hash = models.CharField(max_length=120,null=True,blank=True,verbose_name="Хэш ваших данных",help_text="SHA-256 хэш паспортных данных")

    class Meta:
        # Ограничение на уровне БД
        permissions = [('view_sensitive_date','может просматривать чуствительные данные'),('export_date', 'Может экспортировать данные'),]
        
        # можем установить часто используемые запросы(индексы)
        indexes = [models.Index(fields=['email']), models.Index(fields=['username','is_active']),]

    def clean(self):
        # валидация (провера полей) перед сохранением данных
        super().clean()

        if self.email:
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',self.email):
                raise ValidationError({'email':'неверный формат Email'})
    
    def save(self, *args,**kwargs):
        # переопределяем save для доп. защиты
        self.full_clean() # всегда запусается валидацию проверки данных

        # хешируем чувствительные данные перед сохранением
        if self.ssh_hash and len(self.ssh_hash) < 64: # если это не хэш
            self.ssh_hash = hashlib.sha256(self.ssh_hash.encode()).hexdigest()
        
        super.save(*args,**kwargs)