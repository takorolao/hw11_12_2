from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserProfile
from .mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'restricted.html'
    login_url = '/accounts/login/'