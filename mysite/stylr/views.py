from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
import random


rand_subheads = [
    'Make your style!',
    "Get Stylin'!",
    'Take some inspiration!',
    'Create your outfits!',
]


def generateRand() -> str:
    return rand_subheads[random.randint(0, len(rand_subheads) - 1)]


def home(request):
    retcode = 200
    posts = Post.objects.order_by('-datetimePosted')
    for post in posts:
        post.desc = post.desc[:15]
    context = {
        'title': 'Home',
        'rand_subhead': generateRand,
        'posts': posts,
    }
    return render(request, 'stylr/home.html', context, status=retcode)


def create(request):
    retcode = 200
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.likes = 0
            if len(post.desc) > 200:
                retcode = 400
                form.add_error('desc', 'Description length must be under 200 characters.')
            else:
                post.save()
                return redirect('stylr:home')
    else:
        form = PostForm()
    
    context = {
        'title': 'Create',
        'rand_subhead': generateRand,
        'form': form,
    }
    
    return render(request, 'stylr/create.html', context, status=retcode)


def post_detail(request, id):
    retcode = 200
    post = Post.objects.get(id=id)
    context = {
        'title': f'{post.desc[:10]}...',
        'post': post,
    }
    
    return render(request, 'stylr/posts.html', context, status=retcode)