from django.db import models

# Create your models here.
# Each item should include a picture URL, name, description, and price.

class GarbageModel(models.Model):
    picture=models.URLField()
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name