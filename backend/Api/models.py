from django.db import models


class User(models.Model):
    pass

class Author(models.Model):
    full_name = models.CharField(max_length=32)
    pen_name = models.CharField(max_length=32)
    is_alive = models.BooleanField()
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.full_name



class Publisher(models.Model):
    full_name = models.CharField(max_length=32) # max length is too low
    address = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.full_name


class Translator(models.Model):
    full_name = models.CharField(max_length=32)
    translate_lang = models.CharField(max_length=32)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32) # max length is too low
    author = models.ManyToManyField(Author, related_name="books") # what is related_name?!
    publisher = models.ManyToManyField(Publisher, related_name="books") # what is related_name?!
    translator = models.ManyToManyField(Translator, null=True)
    genre = models.ManyToManyField(Genre, related_name="books") # what is related_name?!
    page_count = models.IntegerField()
    is_exist = models.BooleanField()
    is_published = models.BooleanField(default=True)
    edition_year = models.CharField(max_length=32)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


