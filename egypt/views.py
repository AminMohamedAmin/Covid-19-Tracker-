from django.shortcuts import render
from .models import news, advices, questions, Contacts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from virus.views import Egypt
import requests

# Create your views here.

def home(request):
    egy = Egypt()
    n = news.objects.all()
    d = datetime.now().date()
    paginator = Paginator(n, 5)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'n': n,
        'paginator': paginator,
        'views_title': 'list',
        'query': queryset,
        'page_var': page_var,
        'd': d,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
    }
    return render(request, 'news.html', context)

def advice(request):
    egy = Egypt()
    ad = advices.objects.all()
    d = datetime.now().date()
    paginator = Paginator(ad, 5)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'ad': ad,
        'paginator': paginator,
        'views_title': 'list',
        'query': queryset,
        'page_var': page_var,
        'd': d,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
    }
    return render(request, 'advice.html', context)


def question(request):
    egy = Egypt()
    q = questions.objects.all()
    d = datetime.now().date()
    paginator = Paginator(q, 5)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'q': q,
        'paginator': paginator,
        'views_title': 'list',
        'query': queryset,
        'page_var': page_var,
        'd': d,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
    }
    return render(request, 'question.html', context)

def contact(request):
    egy = Egypt()
    c = Contacts.objects.all()
    d = datetime.now().date()
    paginator = Paginator(c, 5)
    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'c': c,
        'paginator': paginator,
        'views_title': 'list',
        'query': queryset,
        'page_var': page_var,
        'd': d,

        'locationcases': egy.locationcases,
        'locationrecoveries': egy.locationrecoveries,
        'locationdeaths': egy.locationdeaths,
        'locationactive': egy.locationactive,
    }
    return render(request, 'contact.html', context)