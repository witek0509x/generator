from django.db import models


class People(models.Model):
    name = models.CharField(max_length=200)
    asked = models.IntegerField(default=0)
