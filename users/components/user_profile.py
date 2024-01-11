from django_unicorn.components import UnicornView, HashUpdate
from users.models import CustomUserManager
from users.models import User
from django.contrib import messages
from django.contrib import messages

class UserProfileView(UnicornView):
    profile: User = User.objects.none()
    user_id:str
    user_email:str = ""
    user_password = ""
    user_phone = ""
    user_first_name = ""
    user_last_name = ""
    user_data:User = profile
    messages_que:None
    def mount(self):
        self.user_id = self.component_kwargs['user'].pk
        self.profile = User.objects.get(pk=self.user_id)
        self.user_email = self.profile.email
        self.user_phone = self.profile.phone
        self.user_first_name = self.profile.first_name
        self.user_last_name = self.profile.last_name
        return super().mount()
    
    def update_profile(self):
        self.user_data = self.profile
        self.user_data.first_name = self.user_first_name
        self.user_data.last_name = self.user_last_name
        self.user_data.save()
        self.messages_que = messages.success(self.request, "Your profile has been updated successfully!!!")
    

