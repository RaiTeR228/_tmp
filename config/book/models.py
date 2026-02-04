from django.db import models

class Genre(models.Model):
    name_genre = models.CharField(max_length=20,verbose_name="название жанра") #название жанра

class Author(models.Model):
    author = models.CharField(max_length= 50, verbose_name="автор") #автор

    def __str__(self):
        return self.name

class Shelving(models.Model):
    shelving = models.IntegerField(verbose_name="стелаж/шкаф") # стелаж
    shelf = models.ImageField(verbose_name="полка")
    uuid_book = models.ImageField(verbose_name="где находится книга")

    def __str__(self):
        return self.name

class Page(models.Model):
    page = models.IntegerField(verbose_name="страницы") #страницы
    uuid_book = models.ImageField(verbose_name="uuid книги")

    def __str__(self):
        return self.name

class Genre_book(models.Model):
    genre = models.IntegerField(verbose_name="жанр книги")

class Book(models.Model):
    name_book = models.CharField(max_length= 100, verbose_name="название книги") #название книги
    id_book = models.IntegerField(verbose_name="id жанра")
    author_book = models.IntegerField(verbose_name="автор книги")
    
    # прочие
    create_at = models.DateTimeField(auto_now_add=True) # время создание(дата и время)
    in_stock = models.BooleanField(default=True) # в наличии или нет
    uuid = models.UUIDField() # генерация название для книг

    def __str__(self):
        return self.name