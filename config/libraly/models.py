from django.db import models

class Lib(models.Model):
    name_lib = models.CharField(max_length=100,verbose_name="название библиотек") #название библиотеки
    num_book = models.IntegerField(verbose_name="количество книг") # количество книг
    addr = models.CharField(max_length=100, verbose_name="адрес библиотеки") #адрес библиотеки1

    in_stock = models.BooleanField(default=True) # работает/есть ли она или нет библиотека
    create_at = models.DateTimeField(auto_now_add=True) # дата и время создание 
    uuid = models.UUIDField() # генерация название

    def __str__(self):
        return self.name

