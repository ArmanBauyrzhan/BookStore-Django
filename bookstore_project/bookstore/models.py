
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=[('available', 'Available'), ('rented', 'Rented')], default='available'
    )
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.title
