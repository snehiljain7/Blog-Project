from django import forms
from .models import Blog
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('id','title', 'description','image')
        widgets = {'description':forms.Textarea}

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        widgets = {'password': forms.PasswordInput()}
