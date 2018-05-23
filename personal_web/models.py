from django.db import models

# Create your models here.


class personal(models.Model):
    description = models.CharField(max_length=100)#最大限制字数
