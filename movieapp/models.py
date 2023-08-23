from django.db import models
from django.db.models import Model


# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    disc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
