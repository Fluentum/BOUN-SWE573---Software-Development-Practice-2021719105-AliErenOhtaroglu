from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# importing our posts model
from .models import Post, Category

#choices = Category.objects.all().values_list('name', 'name')

#choice_list = []

#for item in choices:
#    choice_list.append(item)

# choices = [('Read', 'Read'), ('Listen', 'Listen'), ('Visit', 'Visit'), ('Watch', 'Watch')]

# helpers are called decorators. pre-written codes for some common tasks.
# imported below to login purpose.

# from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'zenmind/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'zenmind/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView, forms.ModelForm):
    model = Post
    fields = ['title', 'content', 'url', 'category']

#    widgets = {
#       'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
#    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, forms.ModelForm):

    model = Post
    fields = ['title', 'content', 'url', 'category']

#    widgets = {
#       'category': forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
#3    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'

    def test_func(self):

        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):

    return render (request, 'zenmind/about.html', {'title': 'About'})

