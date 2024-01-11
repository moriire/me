from django_unicorn.components import UnicornView
from users.models import Profile, User

class UpdateProfileView(UnicornView):
    profile: Profile = None
    user: User = None
    def mount(self):
        self.profile = Profile.objects.filter(user=self.request.user).first()
        self.user = self.request.user

    def save(self):
        self.profile.save()
        self.user.save()
        self.call('success')