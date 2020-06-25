from django.shortcuts import render
from .models import BlogModel


def AllBlogs(request):
    blogs = BlogModel.objects.all()
    return render(request,'allblogs.html',{'blogs':blogs})

def DynamicUrl(request,title):
    obj = BlogModel.objects.get(blogTitle=title)
    return render(request,'blogs.html',{'obj':obj})