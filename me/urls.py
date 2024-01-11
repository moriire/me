from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms# import ModelForm
class IndexView(TemplateView):
    def get(self, request, pk=None):
        profile = Profile.objects.filter(user__alias = pk).select_related('user').first()
        return render(request, 'index.html', {'profile': profile})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class UploadView(LoginRequiredMixin, TemplateView):
    def get(self, request):
         profile_form = ProfileForm(instance=request.user)
         return render(request, 'upload.html', {
              'profile_form': {}#profile_form
         })
    def post(self, request):
        pic = request.FILES.get('pic')
        profile = Profile.objects.get(user = request.user)
        profile.pic = pic
        profile.save()
        return render(request, 'upload.html', {})
    """
    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            return redirect('myprofile')
        else:
            print('jjjj')
            #messages.error(request, ('Please correct the error below.'))
        return render(request, 'upload.html', {'profile_form':profile_form})
    """

urlpatterns = [
    path('auth/', include('users.urls')),
    path("<str:pk>/me", IndexView.as_view(), name='user-home'),#TemplateView.as_view(template_name='index.html')),
    path("upload/", UploadView.as_view(), name='user-upload'),#TemplateView.as_view(template_name='index.html')),
    path("unicorn/", include("django_unicorn.urls")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [re_path(r'^media/(?P<path>.*)', serve, {
         'document_root': settings.MEDIA_ROOT})]