from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Post
from .forms import PostForm


@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


@login_required(login_url='/accounts/login/')
def new_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.author = request.user
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
    context = {'post': post}

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/post_delete.html', context)


@login_required(login_url='/accounts/login/')
def filter_by_tag(request, tag):
    posts = Post.objects.filter(author=request.user, tags__contains=[tag])
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'blog/post_detail.html'