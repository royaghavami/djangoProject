from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article


def home(request):
    context = {
        "articles": Article.objects.filter(status='p').order_by('-publish')
        # if we wanted to show only last three articles:
        # "articles": Article.objects.filter(status='p').order_by('-publish')[:3]
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    context = {
        "article": Article.objects.get(slug=slug)
        # if we wanted to show only last three articles:
        # "articles": Article.objects.filter(status='p').order_by('-publish')[:3]
    }
    return render(request, "blog/detail.html", context)

# Create your views here.
