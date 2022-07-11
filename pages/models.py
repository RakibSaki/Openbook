from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    content = models.TextField(max_length=2000, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)