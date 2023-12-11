from django.urls import path
from .views import HomePageView, ProfileView, RestrictedView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('restricted/', RestrictedView.as_view(), name='restricted'),
]
