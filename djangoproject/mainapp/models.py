from django.db import models


class UserData(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.FloatField()
    favorite_color = models.CharField(max_length=7)
