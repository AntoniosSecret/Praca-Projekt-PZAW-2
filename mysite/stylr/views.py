from django.shortcuts import render
import random


rand_subheads = [
    'Make your style!',
    "Get Stylin'!",
    'Take some inspiration!',
    'Create your outfits!',
]

def home(request):
    retcode = 200
    rand_subhead = rand_subheads[random.randint(0, len(rand_subheads) - 1)]
    context = {
        'title': 'Home',
        'rand_subhead': rand_subhead,
    }
    return render(request, 'stylr/home.html', context, status=retcode)

def create(request):
    retcode = 200
    context = {
        'title': 'Create',
    }
    return render(request, 'stylr/create.html', context, status=retcode)