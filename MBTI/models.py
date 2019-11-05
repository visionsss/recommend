from django.db import models
from login.models import User


class MBTIType(models.Model):
    mbti_type = models.CharField(max_length=32, unique=True, primary_key=True)
    mbti_analysis = models.CharField(max_length=1024)

    def __str__(self):
        return self.mbti_type

    class Meta:
        ordering = ["mbti_type"]
        verbose_name = "MBTI信息"
        verbose_name_plural = "MBTI信息"

