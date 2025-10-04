from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

#listing model

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# booking model
class Booking(models.Model):
    class Status(models.TextChoices):
        pending = "pending", "Pending"
        confirmed = "confirmed", "Confirmed"
        canceled = "canceled", "Canceled"

    
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.pending)
    created_at = models.DateTimeField(auto_now_add=True)

# review model

class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)