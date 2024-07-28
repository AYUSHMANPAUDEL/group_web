from django.shortcuts import render , HttpResponse ,  get_object_or_404
from .models import blogs
from django.http import HttpResponse, Http404
# Create your views here.
def home(request):
    return render(request,"home/index.html")

def blog_detail(request, blog_name):
    try:
        post = blogs.objects.get(title=blog_name)
    except blogs.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request,"home/blogs_preview.html",{"post": post})
