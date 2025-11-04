from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView , DetailView
from matplotlib.style import context

from .models import Post
# Create your views here.

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 3

class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = context["post"].tags.all()
        return context