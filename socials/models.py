from collections.abc import Iterable
from django.db import models
from django.contrib.auth import get_user_model

User =  get_user_model()

class MediaType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    url = models.URLField(max_length=30, unique=True)
    icon = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_media")
    media = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name="media_type")#, to_field="name")
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name
    
    def link(self):
        return f"{self.media.url}/{self.user_name}"
    
class Social(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_social")
    socials = models.ManyToManyField(Media, related_name="user_social_media", blank=True,)
    def __str__(self):
        return f'{self.user.id}'