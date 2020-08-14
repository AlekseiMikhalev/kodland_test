from django.shortcuts import render, redirect
from django.http import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm



# Create your views here.
class PostList(ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'