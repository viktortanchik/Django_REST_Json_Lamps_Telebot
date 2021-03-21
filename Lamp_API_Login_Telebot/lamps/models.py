from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Lamps(models.Model):
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=64)
    status = models.CharField(verbose_name='status', db_index=True, max_length=64)
    mode = models.CharField(verbose_name='mode', db_index=True,  max_length=64)
    red = models.CharField(verbose_name='red', db_index=True, max_length=64)
    green = models.CharField(verbose_name='green', db_index=True, max_length=64)
    blue = models.CharField(verbose_name='blue', db_index=True, max_length=64)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

class ProgramLamps1(models.Model):
    pixel_1r = models.CharField(verbose_name='pixel_1_red', db_index=True, max_length=64)
    pixel_1g = models.CharField(verbose_name='pixel_1_green', db_index=True, max_length=64)
    pixel_1b = models.CharField(verbose_name='pixel_1_blue', db_index=True, max_length=64)

