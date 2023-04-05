from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView ,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from urllib import request
from django.shortcuts import get_object_or_404
from .models import Post



def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'policy/index.html',context)



def social(request):
    context={
        'posts':Post.objects.filter(category="social")
    }
    return render(request,'policy/index.html',context)

def other(request):
    context={
        'posts':Post.objects.filter(category="other")
    }
    return render(request,'policy/index.html',context)

def sciTech(request):
    context={
        'posts':Post.objects.filter(category="sciTech")
    }
    return render(request,'policy/index.html',context)

def environment(request):
    context={
        'posts':Post.objects.filter(category="environment")
    }
    return render(request,'policy/index.html',context)

def foreign(request):
    context={
        'posts':Post.objects.filter(category="foreign")
    }
    return render(request,'policy/index.html',context)

def economic(request):
    context={
        'posts':Post.objects.filter(category="economic")
    }
    return render(request,'policy/index.html',context)

 





def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect !!!")
    return render(request,'policy/login.html')

@login_required
def LogoutPage(request):
    logout(request)
    return redirect('index')


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'policy/index.html'
    context_object_name = 'posts'
  
    
def PostDetail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    posts = Post.objects.filter(category=post.category).exclude(pk=pk)
    context = {"object":post,'post':post,"posts":posts}
    return render(request,'policy/post_detail.html',context) 



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    
    fields = ['category','title','content','image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['category','title','content','image']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(DeleteView):
    model =Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False