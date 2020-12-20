from django.shortcuts import render, redirect
from . import forms
from .models import Human, Create
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

#from .views_cases import humanRegistration, create_registration_form

import requests

#OPENWEATHERMAP_TOKEN = 'api.openweathermap.org/data/2.5/weather?q={Almaty}&appid={e7c667c341fba44ed5a836470b1d2f96}'

#def weath(request):
 #   if request.method == "POST":
  #      api_connect(request.POST['city_name'])
   # return render(request, 'Check/weather.html')


#def start(request):
 #   context = create_registration_form()
  #  if request.method == "POST":
   #     return humanRegistration(request, context)
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(request, username = username, password = password)
        #if user is not None:
            #login(request, user)
            #return redirect('show')
        #else:
            #context['errors'] = "Invalid login or password"
    #return render(request, 'Check/login.html', context)



def loginning(request):
    context = {
        'form': forms.UsersForm(),
        'errors': ""
        }
    if request.method == "POST":
        username =  request.POST['username'] 
        password =  request.POST['password'] 
        user = User.objects.get( username = username, password = password) 
        if user is not None:
            login(request, user)
            return redirect('diarymain')
        else:
            context['errors'] = "Invalid login or password"
    #if request.method == "POST":
       # arr = User.objects.all()
        # Human.objects.get(username="Alex")
        # Human.objects.filter(username="Alex")
        # Human.objects.exclude(username="Alex")
        # k = 0
       # for user in arr:
         #   if human.username == request.POST['username'] or human.email == request.POST['email']:
          #      k = 1
        #if request.POST['pas'] != request.POST['pas1']:
          #  context['errors'] = "Input data aren't equal!"
       # if k == 1:
           # context['errors'] = "Invalid username or email!"
       # else:
           # person = User()
           # person.username = request.POST['username']
           # person.email = request.POST['email']
          #  person.password = request.POST['password']
           # person.save()
        
    return render(request, "Check/login.html", context)


#def picture(request):
 #   return render(request, 'Check/img.html')

#def handle_upload_file(file, name, postfix):
 #   with open(f'media/avatars/{name}{postfix}', 'wb+') as dest:
  #      for chunk in file.chunks():
   #         dest.write(chunk)

#def upload(request):
 #   it = Item.objects.get(i=5)
  #  context = {
   #     'form':forms.AvatarUpload(),
    #    'photo':it.avatar}
    #if request.method == "POST":
     #   name = request.FILES['avatar'].name
      #  postfix = request.FILES['avatar'].name
       # postfix = request.FILES['avatar'].name[name.rfind('.'):]
        #name = name[:name.rfind(".")]
        #handle_upload_file(request.FILES['avatar'], name, postfix)
        #item = Item.objects.get(i=5)
        #item.avatar = request.FILES('avatar')
        #item.save()
    #return render(request, "Check/upload.html", context)


def registration(request):
    context = {
        'form':forms.RegistrationForm(),
        'errors': ""

    }
    if request.method == "POST":
        arr = Human.objects.all()
        person = Human()
        person.username = request.POST['username']
        person.email = request.POST['email']
        person.pas = request.POST['pas']
        person.pas1 = request.POST['pas1']
        k = 0 
        for human in arr:
            if person.username == request.POST['username'] or person.email == request.POST['email']:
                 k = 1
        if request.POST['pas'] != request.POST['pas1']:
            context['errors'] = "Input data aren't equal!"
        elif k == 1:
            context['errors'] = "Invalid username or email"

        else:
            person.save()
    return render(request, "Check/registration.html", context)

def diarymain(request):
    context = {
        'user':request.user
        #'create':request.create

    }
    return render(request, "Check/diarymain.html", context)

def diarycreating(request):
    context = {
        'form': forms.CreateForm(),
       # 'exclude':Create.objects.exclude(task = request.create.task)
        'errors': ""
        }
    if request.method == "POST":
        task =  request.POST['task'] 
        create = User.objects.get(email=email) 
        if create is not None:
            diarycreate(request, create)
            return redirect('diarymain')
        else:
            context['errors'] = "Invalid"
    
    return render(request, "Check/diarycreate.html")

def diarydelete(request):
    return render(request, "Check/diarydelete.html")
    







# Create your views here.
