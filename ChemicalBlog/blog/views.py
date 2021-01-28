from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles,Interview,News;
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    allInts = Interview.objects.all()
    a=len(allInts)
    allInt=reversed(allInts[abs(a-3):])
    allBlogs = Articles.objects.all()
    a=len(allBlogs)
    allBlog = reversed(allBlogs[a-3:])
    context={'allInt':allInt,'allBlog':allBlog}
    return render(request,'index.html',context)

def news(request):
    return render(request,'news.html')

def interview(request):
    allBlog = Interview.objects.all().order_by('-pub_date')
    page_n = request.GET.get('page', 1)
    p = Paginator(allBlog,3)
    try:
        page = p.page(page_n)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)
    context = {'allBlogs': allBlog, 'page': page}
    return render(request, 'interview.html', context)

def blog(request):
    allBlog=Articles.objects.all().order_by('-pub_date')
    page_n=request.GET.get('page',1)
    p = Paginator(allBlog, 3)
    try:
        page=p.page(page_n)
    except PageNotAnInteger:
        page=p.page(1)
    except EmptyPage:
        page=p.page(p.num_pages)
    context={'allBlogs':allBlog,'page':page}
    return render(request,'blog.html',context)

def post(request,slug):
    post=Articles.objects.get(article_title__contains=slug)
    context={'blogs':post}
    return render(request,'post.html',context)

def intpost(request,slug):
    post=Interview.objects.get(interview_title__contains=slug)
    context={'blogs':post}
    return render(request,'post.html',context)