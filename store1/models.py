from django.db import models

# Create your models here.
class Toys(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    describe = models.TextField(default = 'New Toys')
    price = models.FloatField()
    def __str__(self):
        return self.name