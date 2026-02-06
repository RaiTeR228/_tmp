# сериализация с валидацией и защитой пароля
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User
# разделеяяем сериализаторы на каждую отдельную классовую задачу
class UserCreateSerializer(serializers.ModelSerializer):
    # только для создание пользователя
    password = serializers(writly_only = True, required = True, validate = [validate_password])

    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        # Хэшируем пароль перед сохранением
        user = User.objects.create_user(**validated_data)
        return user

# ==== создать разные сериализаторы для типов передаци данных
"""
- для неавторизованных пользователей
- для авторизованных
- только для админов
- защита от массового присвоения запрещать менять важные поля
- всегда явно указывается через [] какие именно поля должны обрабатыватся
"""