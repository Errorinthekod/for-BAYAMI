from django.db import models

from django.db import models

# Create your models here.

# Create your models here.


class About(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')