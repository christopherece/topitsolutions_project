from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from datetime import datetime
from tinymce import models as tinymce_models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    body = tinymce_models.HTMLField()
    comment = models.CharField(max_length=200, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title


