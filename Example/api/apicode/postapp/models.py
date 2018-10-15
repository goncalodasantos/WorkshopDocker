from django.db import models


# Create your models here.


class Post(models.Model):
    comment = models.CharField(max_length=200)