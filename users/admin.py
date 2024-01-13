from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from users.models import Profile, Section, User
#User = get_user_model()
admin.site.register(Profile)
admin.site.register(Section)
admin.site.register(User)
"""
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #change_form_template = "admin/auth/user/change_form.html"
    #change_list_template = "admin/auth/user/change_list.html"
    #list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('email',)
    ordering = ('pk',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
"""