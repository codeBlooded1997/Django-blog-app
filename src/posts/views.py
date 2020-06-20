from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    # We need to specify the fields that we want to allow user to update
    # Here we can only specify fields or form. We cannot specify both
    form_class = PostForm
    model = Post
    success_url = '/'

    # passing context into the view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class PostUpdateView(UpdateView):
    # We need to specify the form we want to display to user
    form_class = PostForm
    model = Post
    # Redirect to following
    success_url = '/'

    # passing context into the view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    # THis is the url to redirect
    success_url = '/'
