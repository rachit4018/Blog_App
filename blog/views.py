from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Post
# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'text']

class BlogUpdateView(UpdateView):
    model =Post
    template_name = 'post_update.html'
    fields = ['title','text']
