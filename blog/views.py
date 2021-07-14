
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.publish.all()
    return render(request,'blog/post/list.html',{'post':posts})

