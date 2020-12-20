from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render

import requests



def humanRegistration(request, context):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('show')
    else:
        context['errors'] = "Invalid login or password"   

def create_registration_form():
    context = {
        'from': UsersForm(),
        'errors':""
    }
    return context 


#def api_connect(city_name):
    #url = f'api.openweathermap.org/data/2.5/weather?q={ }&appid={e7c667c341fba44ed5a836470b1d2f96}'

    #info = requests.get(url).json()
    #final_info = {
        #'city':info['name'],
        #'weather':info['weather'][0]['main'],
        #'desc':info['weather'][0]['description'],
        #'temperature':int(info['main']['temp']-273),
        #'feels_like':int(info['main']['feels_like']-273),
        #'pressure':info['main']['pressure'],
        #'humidity':str(info['main']['humidity']) + "%",
       # 'country':info['sys']['country']}

    #api_connect('Almaty')