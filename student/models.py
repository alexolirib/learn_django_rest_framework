from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    discount = models.BooleanField(default=False)


    #authenticated
    #owner = models.ForeignKey('auth.User', related_name='students', on_delete=models.CASCADE)
    #highlighted = models.TextField()


    class Meta:
        ordering = ('name',)
        app_label='student'
