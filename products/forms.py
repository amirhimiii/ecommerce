from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("title",'stars')

# class CommentForm(forms.Form):
#     text = form



    
    
