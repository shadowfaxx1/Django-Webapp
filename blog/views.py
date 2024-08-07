from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.conf import settings
from .models import Post 
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


import pprint
from django.views.generic import TemplateView


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering= ['-date_posted']
 
    paginate_by =5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    paginate_by =5
    
    def get_query_set(self):
        user = get_object_or_404(User,username=self.kwargs.get('user'))
        return Post.objects.filter(author= user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author= self.request.user
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author= self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
class PostDeletelView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


#class based view :
# - list view , details , create , delete ,update views 
