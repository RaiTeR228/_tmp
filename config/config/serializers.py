from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name_book = serializers.CharField(max_length=100)
    id_book = serializers.IntegerField()
    author_book = serializers.IntegerField()
    create_at = serializers.DateTimeField(read_only=True)
    in_stock = serializers.BooleanField()
    uuid = serializers.UUIDField()
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name_book = validated_data.get('name_book', instance.name_book)
        instance.id_book = validated_data.get('id_book', instance.id_book)
        instance.author_book = validated_data.get('author_book', instance.author_book)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.save()
        return instance