from django import forms

class PostForm(forms.Form):
    image = forms.ImageField()
    
    
    pass