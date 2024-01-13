from django.contrib import admin
from .models import Media, Social, MediaType
admin.site.register(MediaType)
admin.site.register(Media)
admin.site.register(Social)