from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Librarian(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey('Library', on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.OneToOneField(Librarian, on_delete=models.CASCADE)
