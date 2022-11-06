from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class homepageView(View):
    template_name='blog/index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class aboutView(View):
    template_name='blog/about.html'
    
    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {})

class PostListView(ListView):
    model=Post
    template_name='blog/blog-list.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5
    
    def get_context_data(self, request, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title', 'body', 'image']='Post'
        return context


class PostDetailView(DetailView):
    model=Post
    template_name='blog/blog-post.html'
    context_object_name='post'
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class createDetailView(CreateView):
    model=Post
    template_name='blog/post_form.html'
    fields=['title','body','date_posted']
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class updateDetailView(UpdateView):
    model=Post
    
    
class deleteDetailView(DeleteView):
    model=Post

