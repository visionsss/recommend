from django.db import models


class school_info(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rank = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128)
    special = models.CharField(max_length=128, blank=True)
    belong = models.CharField(max_length=128)
    type1 = models.CharField(max_length=128)
    type2 = models.CharField(max_length=128)
