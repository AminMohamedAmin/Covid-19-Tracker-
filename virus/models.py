from django.db import models

# Create your models here.


class Assure(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    temperature = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    throat = models.BooleanField(default=False)
    vomiting = models.BooleanField(default=False)
    chronic = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)
    respiratory = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    visiting = models.BooleanField(default=False)
    worker = models.BooleanField(default=False)

    class Meta:
        ordering = ('address',)
        verbose_name = "Assure"
        verbose_name_plural = "Assures"
