from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category
from blogs.models import Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    
    try:
        about = About.objects.get() #get will fetch only one data  

    except:
        about = None    

    context = {
         'featured_posts':featured_posts,
         'posts' :posts,
         'about':about,
    }
    return render(request,'home.html',context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
      form = RegistrationForm()
    context ={
        'form': form,
    }
    return render(request, 'register.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()   # ✅ better way
            
            auth.login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')