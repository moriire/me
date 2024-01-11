from django.db import models
from django.contrib.auth import get_user_model
User =  get_user_model()
class Media(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_media_link")
    link = models.URLField()
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Social(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_social")
    socials = models.ManyToManyField(Media, related_name="user_social_media")
