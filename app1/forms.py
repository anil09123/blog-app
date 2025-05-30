from django import forms 
from .models import Post 
 
class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ['title', 'content'] 
        widgets = { 
            'title': forms.TextInput(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Enter post title' 
            }), 
            'content': forms.Textarea(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Write your content here...', 
                'rows': 5 
            }), 
        } 
        labels = { 
            'title': 'Post Title', 
            'content': 'Content', 
        } 