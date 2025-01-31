from django.shortcuts import render
import random


rand_subheads = [
    'Make your own style!',
    'Start Stylizing!',
    'Take some inspiration!',
    'Create your outfits!',
]

def home(request):
    retcode = 200
    context = {
        'title': 'Home',
        'rand_subhead': rand_subheads[random.randint(0, len(rand_subheads) - 1)],
    }
    return render(request, 'stylr/home.html', context, status=retcode)
