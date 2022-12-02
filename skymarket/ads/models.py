from django.conf import settings
from django.db import models

# from skymarket.users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(blank=False, max_length=400, unique=True, null=False)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

