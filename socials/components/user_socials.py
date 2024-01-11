from django_unicorn.components import UnicornView
from socials.models import Media

class UserSocialsView(UnicornView):
    media: Media = Media.objects.none()
    def mount(self):
        self.media.user = self.request.user
    def save_social(self):
        self.media.save()