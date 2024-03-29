from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import json

from .calculator import Calculator

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserData(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
    favorite_color = models.CharField(max_length=7)

    def calculate_psychodata(self):
        calc = Calculator(self.date_of_birth)
        numbers = calc.get_all_numbers_str()
        json_data = json.dumps(numbers)
        return json_data