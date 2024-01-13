from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Media, Social

@receiver(post_save, sender=Media)
def create_item_with_images(sender, created, instance, **kwargs):
    social = Social.objects.get(user = instance.user)
    if created:
        social.socials.add(instance)