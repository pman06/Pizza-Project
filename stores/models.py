from django.db import models
from django.core.validators import RegexValidator


class Pizzeria(models.Model):
    """Model for pizza outlets"""
    phone_validator = RegexValidator(regex=r'^\1?\d{9,10}$')

    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(
        validators=[phone_validator],
        max_length=10,
        blank=True
    )
    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        upload_to='pizzariaImages',
        blank=True,
        default="pizzariaImages/pizzalogo.png"
        )
    email = models.EmailField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.pizzeria_name
