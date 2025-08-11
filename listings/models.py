from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User 

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

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    date_favorited = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'listing')

    def __str__(self):
        return f'{self.user.username} favorites {self.listing.title}'

   