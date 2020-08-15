from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader

# Create your views here.


def home(request):
  # Docuementaion at https://sv443.net/jokeapi/v2/#try-it
    url = 'https://sv443.net/jokeapi/v2/joke/Any'
    response = requests.get(url)
    jokes = response.json()
    joke = ''
    if jokes['type'] == "single":
        joke = jokes['joke']
    else:
        joke = 'Binod:  '
        joke += jokes['setup']
        joke += '\n \n'
        joke += 'Carry:  '
        joke += jokes['delivery']
    template = loader.get_template('joke_home.html')
    context = {
        'jokes': joke,
    }
    return HttpResponse(template.render(context, request))
