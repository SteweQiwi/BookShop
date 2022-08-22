from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    FOLKLORE = 1
    DRAMA = 2
    POETRY = 3
    PROSE = 4
    GENRES = (
        (FOLKLORE, 'Folklore'),
        (DRAMA, 'Drama'),
        (POETRY, 'Poetry'),
        (PROSE, 'Prose')
    )

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.IntegerField(choices=GENRES, null=True)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()


class Shop(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.IntegerField()
    books = models.ManyToManyField('Book', through='InStock')

    @property
    def full_address(self):
        return f"{self.country}, {self.region}, {self.city}, {self.street}, {self.house}"


class BookSold(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    purchase = models.ForeignKey('Purchase', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class InStock(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Purchase(models.Model):
    client = models.CharField(max_length=50, null=True)
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT)
    books = models.ManyToManyField('Book', through='BookSold')
    full_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
