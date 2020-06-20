from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    # We need to specify the fields that we want to allow user to update
    fields = (
        'title',
        'content',
        'tumbnail',
        'author',
        'slug',
    )
    model = Post


class PostDeleteView(DeleteView):
    model = Post
