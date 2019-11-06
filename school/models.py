from django.db import models


class school_info(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rank = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128)
    special = models.CharField(max_length=128, blank=True)
    belong = models.CharField(max_length=128)
    type1 = models.CharField(max_length=128)
    type2 = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["city"]
        verbose_name = "学校信息"
        verbose_name_plural = "学校信息"
