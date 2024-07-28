from django.db import models
from django.utils import timezone

# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    blog_url = models.CharField(max_length=200,default="")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title