from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Coupon(models.Model):
    discount_code = models.CharField(max_length=50, unique=True) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    valid = models.BooleanField()

    def __str__(self):
        return self.discount_code
