from django_unicorn.components import UnicornView, QuerySetType
from socials.models import Media, Social, MediaType
from users.models import User

class UserSocialsView(UnicornView):
    media: Media = Media()
    medias: QuerySetType[Media] = Media.objects.none()
    media_types: MediaType = MediaType.objects.none()
    user_name:str=''
    name:str = ''
    user:User

    def mount(self):
        self.user = self.request.user
        self.media_types = MediaType.objects.all()
        self.update()

    def save_social(self):
        #self.media.media = self.media_types.filter(pk = self.name).first()
        print(self.name)
        media =  MediaType.objects.filter(name = self.name).first()
        obj = Media(
            user = self.user,
            media =  media,
            user_name = self.user_name
        )
        obj.save()
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
        