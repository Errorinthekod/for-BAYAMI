from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-created_at') # одно и тоже

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() # одно и тоже
        context['last_post'] = Post.objects.all()[:3]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() # одно и тоже
        context['last_post'] = Post.objects.all()[:3]
        return context



























