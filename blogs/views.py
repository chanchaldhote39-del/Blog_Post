from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Category
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def post_by_category(request,pk):
    # fetch the post that belongs to category with the id pk
    posts = Blog.objects.filter(status='published',pk=pk)
    try:
        category = Category.objects.get(pk=pk)
    except:
        # redirect to home page
        return   redirect('home')
#    redirect(category = get_object_or_404(category, pk=pk)) i f we want to show error page if id does not exist

    context = {
        'posts' : posts,
        'category':category,
    }
    return render(request, 'post_by_category.html',context)
