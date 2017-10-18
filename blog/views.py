# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect,get_object_or_404

from django.http import HttpResponse



from django.shortcuts import render

# Create your views here.

def post_list(request):
    posts=Post.objects.all();
    return render(request,'blog/index.html',{'posts':posts})

def post_details(request , pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request , 'blog/details.html',{'post':post})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
        return redirect('blog:post_list')

    else:
        form=PostForm()
        return render(request, 'blog/new.html' , {'form':form})

