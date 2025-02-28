from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
        retcode = 400
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
        retcode = 400
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
                post.likes = 0
                if len(post.desc) > 200:
                    retcode = 400
                    form.add_error('desc', 'Description length must be under 200 characters.')
                else:
                    post.user = request.user
                    post.save()
                    return redirect('stylr:home')
        else:
            form = PostForm()
        
        context['form'] = form
        return render(request, 'stylr/create.html', context, status=retcode)


def post_detail(request, id):
    if not request.user.is_authenticated:
        retcode = 400
        return redirect('stylr:login_user')
    else:
        retcode = 200
        post = Post.objects.get(id=id)
        context = {
            'title': f'{post.desc[:10]}...',
            'rand_subhead': generateRand,
            'post': post,
        }
        
        return render(request, 'stylr/posts.html', context, status=retcode)


def login_user(request):
    if request.user.is_authenticated:
        retcode = 400
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
                    return redirect('stylr:home')
                else:
                    return redirect('stylr:login_user')
        else:
            form = LoginForm()
        
        context['form'] = form

        return render(request, 'stylr/login.html', context, status=retcode)


def register_user(request):
    if request.user.is_authenticated:
        retcode = 400
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
                return redirect('stylr:login_user')
        else:
            form = RegisterForm()
        
        context['form'] = form
        
        return render(request, 'stylr/register.html', context, status=retcode)


def logout_user(request):
    logout(request)
    return redirect('stylr:login_user')


def profile(request):
    if not request.user.is_authenticated:
        retcode = 400
        return redirect('stylr:login_user')
    else:
        retcode = 200
        context = {
            'title': f'Profile: {request.user}',
            'rand_subhead': generateRand,
        }
        
        user_posts = Post.objects.filter(user=request.user)
        
        context['user_posts'] = user_posts
        
        return render(request, 'stylr/profile.html', context, status=retcode)