from django_unicorn.components import UnicornView, QuerySetType
from socials.models import Media, Social

class UserSocialsView(UnicornView):
    media: QuerySetType[Media] = Media()
    link = ''
    user = None

    def mount(self):
        self.media.name = 'Linkedin'
        self.media.user = self.request.user

    def save_social(self):
        obj = self.media.save()
        s = Social.objects.get(user = self.user)
        s.user_social_media.add(obj)
        self.clear()

    def clear(self):
        self.name = ''
        self.link = ''