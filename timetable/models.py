from django.db import models


class Band(models.Model):
    band_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)


class BandReg(models.Model):
    band_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField()
