from pickle import FALSE, TRUE
from django.db import models
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class Tagam(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)

    def get_absolute_url(self):
        return f'/project1/{self.id}'

class Makal(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=250)

class Pikir(models.Model):
    title = models.TextField(blank=True)



    def get_number(self):
        return ''
     
    def str(self):
        return self.title

     