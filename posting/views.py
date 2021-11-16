from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

# Create your views here.

class PostList(ListView):
    model = Post

