from django.shortcuts import render
from django.conf import settings
from .models import Post 
# Create your views here.
from django.contrib.auth.decorators import login_required

import pprint


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
