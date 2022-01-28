from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    authors = models.ManyToManyField(Author, through='BookAuthor')
    published_date = models.PositiveSmallIntegerField(
        default=1000,
        validators=[
            MaxValueValidator(2022),
            MinValueValidator(1000)
        ]
    )
    categories = models.ManyToManyField(Category, through='BookCategory')
    average_rating = models.PositiveSmallIntegerField(default=0)
    ratings_count = models.PositiveSmallIntegerField(default=0)
    thumbnail = models.CharField(max_length=300, default="")

    def __str__(self) -> str:
        return self.title

class BookAuthor(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)

class BookCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)


# docker-compose run web python3 manage.py migrate