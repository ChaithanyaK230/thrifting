from django.db import models
from django.utils import timezone

class Listing(models.Model):
    CATEGORY_CHOICES = (
        ('Apparel', 'Apparel'),
        ('Electronics', 'Electronics'),
        ('Home Decor', 'Home Decor'),
        ('Books', 'Books'),
        ('Collectibles', 'Collectibles'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    image = models.ImageField(upload_to='listing_images/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title