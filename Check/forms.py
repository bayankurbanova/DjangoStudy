from django.forms import ModelForm, TextInput, FileInput
from django.contrib.auth.models import User
from .models import Human,Create

#class AvatarUpload(ModelForm):
 #   class Meta:
  #      model = Item
   #     fields = [
    #        'avatar'   ]
        #widgets = {
         #   'avatar':FileInput(attrs = {
          #      "type":"file",
           #     "name":"avatar"})}


class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email'
        ]

        widgets = {
            'username': TextInput(attrs ={
                'class': "text",
                'type': "text",
                'name': "username",
                'placeholder': "Username",
                'required':""
             }),
    

            'email': TextInput(attrs = {
                'class': "text email",
                'type': "email",
                'name': "email", 
                'placeholder': "Email",
                'required': ""
            }),
        
            'pas': TextInput(attrs = {
                'class': "text",
                'type': "password",
                'name': "password", 
                'placeholder': "Password" ,
                'required':""
            })
}

class RegistrationForm(ModelForm):
    class Meta:
        model = Human
        fields = [
            'username',
            'email',
            'pas',
            'pas1'
         ]

        widgets = {
            'username': TextInput(attrs ={
                'class': "text",
                'type': "text",
                'name': "username",
                'placeholder': "Username",
                'required':""
             }),
    

            'email': TextInput(attrs = {
                'class': "text email",
                'type': "email",
                'name': "email", 
                'placeholder': "Email",
                'required': ""
            }),
        
            'pas': TextInput(attrs = {
                'class': "text",
                'type': "password",
                'name': "password", 
                'placeholder': "Password" ,
                'required':""
            }),

            'pas1': TextInput(attrs={
                'class': "text w3lpass",
                'type': "password",
                'name': "password1", 
                'placeholder': "Confirm Password", 
                'required': ""
            })

    }

class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = [
            'task'
         ]
        widgets = {
            'task': TextInput(attrs ={
                'class': "text",
                'type': "text",
                'name': "task",
                'placeholder': "Task",
                'required':""
                 })
        }