from django.urls import path, include
from users.views import IndexView, ProfileView,  AboutView, ContactView, signup_view, activation_sent_view, activate

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('profile/<str:pk>', ProfileView.as_view(), name="profile"),
    path('register/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]