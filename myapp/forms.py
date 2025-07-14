from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
#register
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'shadow appearance-none border [border-image:linear-gradient(45deg,#00c6ff,#0072ff)_1] rounded w-full py-2 px-3 gradient-text leading-tight focus:outline-none focus:shadow-outline'
            if field_name == 'password1' or field_name == 'password2':
                self.fields[field_name].widget.attrs['placeholder'] = "Enter password"
            else:
                self.fields[field_name].widget.attrs['placeholder'] = field_name.capitalize()
        
        
#authenticate a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border [border-image:linear-gradient(45deg,#00c6ff,#0072ff)_1] rounded w-full py-2 px-3 gradient-text leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'shadow appearance-none border [border-image:linear-gradient(45deg,#00c6ff,#0072ff)_1] rounded w-full py-2 px-3 gradient-text leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Password'}))