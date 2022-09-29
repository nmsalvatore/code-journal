from http.client import HTTPResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Post
from .forms import PostForm


@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


@login_required(login_url='/accounts/login/')
def new_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'blog/post_new.html', context)


@login_required(login_url='/accounts/login/')
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('view-post', post.slug)

    context = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', context)


@login_required(login_url='/accounts/login/')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'blog/post_detail.html'