from django.db import models

# Create your models here.


class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField()

    