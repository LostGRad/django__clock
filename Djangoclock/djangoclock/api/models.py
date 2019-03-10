from django.db import models

class ClockGmt(models.Model):
    text = models.CharField(max_length= 256)
    gmt = models.IntegerField()


# Create your models here.
