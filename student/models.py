from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    discount = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
