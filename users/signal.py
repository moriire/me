from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_item_with_images(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.user_profile.save()
