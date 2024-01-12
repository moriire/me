from django_unicorn.components import UnicornView, QuerySetType
from socials.models import Media, Social
from users.models import User
class UserSocialsView(UnicornView):
    media: QuerySetType[Media] = Media()
    medias: Media = Media.objects.none()
    user:User

    def mount(self):
        self.user = self.request.user
        obj = Social.objects.get(user=self.request.user)
        print(obj.socials.count())
        self.media.name = 'Linkedin'
        self.media.user = self.request.user
        self.update()

    def save_social(self):
        self.media.save()
        self.update()
        self.clear()

    def delete_social(self, social_to_delete: Media):
        social_to_delete.delete()
        self.update()

    def save_single_social(self, social_to_save: int):
        self.medias[social_to_save].save()
        self.update()

    def update(self):
        self.medias = Media.objects.filter(user = self.user)

    def clear(self):
        self.reset()
        self.media.name = ''
        self.media.link = ''