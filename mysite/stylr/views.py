from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import PostForm, LoginForm, RegisterForm
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
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access page.")
        return redirect('stylr:login_user')
    else:
        retcode = 200
        posts = Post.objects.order_by('-datetimePosted')
        query = request.GET.get('searchbar', '')
        if query:
            posts = posts.filter(desc__icontains=query)
        
        for post in posts:
            post.desc = post.desc[:15]
        context = {
            'title': 'Home',
            'rand_subhead': generateRand,
            'posts': posts,
            'query': query,
        }
        return render(request, 'stylr/home.html', context, status=retcode)


def create(request):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access page.")
        return redirect('stylr:login_user')
    else:
        context = {
            'title': 'Create',
            'rand_subhead': generateRand,
        }
        retcode = 200
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                if len(post.desc) > 200:
                    retcode = 400
                    messages.error(request, "Description length must be under 200 characters.")
                else:
                    post.user = request.user
                    post.save()
                    messages.success(request, "You've successfully posted.")
                    return redirect('stylr:home')
        else:
            form = PostForm()
        
        context['form'] = form
        return render(request, 'stylr/create.html', context, status=retcode)


def post_detail(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access page.")
        return redirect('stylr:login_user')
    else:
        retcode = 200
        post = Post.objects.get(id=id)
        context = {
            'title': f'{post.desc[:10]}...',
            'rand_subhead': generateRand,
            'post': post,
            'likes': post.num_of_likes(),
        }
        
        return render(request, 'stylr/posts.html', context, status=retcode)


def login_user(request):
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect('stylr:home')
    else:
        retcode = 200
        context = {
            'title': 'Login',
        }
        
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, "You've successfully logged in.")
                    return redirect('stylr:home')
                else:
                    return redirect('stylr:login_user')
        else:
            form = LoginForm()
        
        context['form'] = form

        return render(request, 'stylr/login.html', context, status=retcode)


def register_user(request):
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect('stylr:home')
    else:
        retcode = 200
        context = {
            'title': 'Register',
        }
        
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "You've successfully registered an account.")
                return redirect('stylr:login_user')
        else:
            form = RegisterForm()
        
        context['form'] = form
        
        return render(request, 'stylr/register.html', context, status=retcode)


def logout_user(request):
    logout(request)
    messages.success(request, "You've successfully logged out.")
    return redirect('stylr:login_user')


def profile(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access page.")
        return redirect('stylr:login_user')
    else:
        retcode = 200
        context = {
            'rand_subhead': generateRand,
        }
        
        user = User.objects.get(id=id)
        
        user_posts = Post.objects.filter(user=user).order_by('-datetimePosted')
        
        context['user'] = user
        context['title'] = f'Profile: {user}'
        context['user_posts'] = user_posts
        
        return render(request, 'stylr/profile.html', context, status=retcode)


def like_post(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access page.")
        return redirect('stylr:login_user')
    else:
        post = Post.objects.get(id=id)
        
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    
        return redirect(reverse('stylr:post_detail', args=[post.id]))