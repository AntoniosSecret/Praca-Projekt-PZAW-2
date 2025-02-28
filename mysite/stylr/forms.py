from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label_suffix = ''
        self.fields['desc'].required = False
    
    class Meta:
        model = Post
        fields = ['image', 'desc']
        labels = {
            'image': 'Select Image',
            'desc': '',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-file-input'}),
            'desc': forms.Textarea(attrs={'class': 'form-text-input', 'placeholder': 'Enter a description....'}),
        }


class LoginForm(forms.Form):
    
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput,
    )
    
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'id': 'usernameInput',
            'autofocus': 'True',
        })

        self.fields['username'].label = 'Username'
        self.fields['username'].label_suffix = ''

        self.fields['password'].widget.attrs.update({
            'class': 'form-input',
            'id': 'passwordInput',
        })

        self.fields['password'].label = 'Password'
        self.fields['password'].label_suffix = ''


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'id': 'usernameInput',
        })

        self.fields['username'].label = 'Username'
        self.fields['username'].label_suffix = ''
        self.fields['username'].help_text = 'Max. 150 characters.'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'id': 'password1Input',
        })

        self.fields['password1'].label = 'Password'
        self.fields['password1'].label_suffix = ''
        self.fields['password1'].help_text = 'Minimum 8 characters.'

        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'id': 'password2Input',
        })

        self.fields['password2'].label = 'Repeat Password'
        self.fields['password2'].label_suffix = ''
        self.fields['password2'].help_text = 'Repeat password for verification.'