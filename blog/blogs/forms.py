from os import error
from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= "__all__"
        labels = {
            "name":"Your Name",
            "email": "Your Email",
            "content":"Comment"
        }
        error_messages = {
            "name": {
                "required":"Name cannot be Empty",
                "max_length":"Please Enter a Shorter Name"
            }
        }

class Commentsformclass(forms.Form):
    name = forms.CharField(label= "Your Name",max_length=30,error_messages={
        "required":"Name cannot be Empty",
        "max_length":"Please Enter a Shorter Name"
    })
    email = forms.EmailField()
    content = forms.CharField(label="Comment",widget=forms.Textarea)


class picform(forms.Form):
    pic = forms.FileField()