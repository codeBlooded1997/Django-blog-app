from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, **kwargs):
        """
        This method handles the view count.
        """
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated():
            # get_or_created: if you visit the website twice,
            # it wount count two times, but it will couse error
            # to anonymous users
            PostView.objects.get_or_create(user=self.request.user, post=object)
        # Otherwise don't do anything
        return object


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


# this method is going to handle the liking and disliking proccess
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        # Unlike the post
        like_qs[0].delete()
        return redirect('detail', slug=slug)

    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
