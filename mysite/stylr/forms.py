from django import forms
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