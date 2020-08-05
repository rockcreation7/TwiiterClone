import random
from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']
    
    def serialize(x):
        return {
            "id": x.id,
            "content": x.content,
            "likes": random.randint(0, 200)
        }
