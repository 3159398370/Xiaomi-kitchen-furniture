# xiaomijiaju/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=[
        ('储物', '厨房储物'),
        ('桌台', '厨房桌台'),
        ('电器', '厨房电器'),
    ], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return '/static/img/placeholder.jpg'

class InstallationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    product = models.CharField(max_length=50)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.product}"