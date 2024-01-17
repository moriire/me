from django_unicorn.components import UnicornView
from users.models import Profile, User

class UpdateProfileView(UnicornView):
    profile: Profile = None
    user: User = None
    msg:str = ""
    cls:str = ""
    def mount(self):
        self.profile =self.request.user.user_profile#  Profile.objects.filter(user=self.request.user).first()
        self.user = self.request.user

    def message(self, cls, msg):
        self.msg = msg
        self.cls = cls
        self.call('success')
        
    def save(self):
        self.profile.save()
        self.user.save()
        self.message('success', "Profile updated successfully!")