from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def django(request):
    posts = Post.objects.all()
    return render(request, 'blog/django.html')
def web(request):
    posts = Post.objects.all()
    return render(request, 'blog/web.html')
def g(request):
    posts = Post.objects.all()
    return render(request, 'blog/g.html')