from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    new_post = Post.objects.all()
    return render(request, 'index.html', {'posts': new_post})

def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        new_post = Post.objects.create(title=title, body=body)
        new_post.save
        return redirect('http://127.0.0.1:8000/')
    else:
        return render(request, 'newpost.html')

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})