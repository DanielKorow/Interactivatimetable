from django.db import models


class Band(models.Model):
    band_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)


class BandReg(models.Model):
    band_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=12, default="")


class Repetition(models.Model):
    band = models.ForeignKey(Band, default="")
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    date = models.CharField(max_length=12)
