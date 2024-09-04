from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from ..post.models import *
from .models import About
from ..post.views import Post, Category
# Create your views here.



class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posta'] = Post.objects.all()[:3]
        context['categories'] = Category.objects.all() # одно и тоже

        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'



class AboutPageView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all() # одно и тоже
        return context








































