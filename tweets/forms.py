from django import forms
from uuid import uuid4
import os
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message", 
                            "class": "form-control","style" :"background:#FFF; font-size:28px","rows":"3"}
                    ))
    # image = forms.ImageField(label='Add an image',required=False)
    
    class Meta:
        model = Tweet
        fields = [
            #"user",
            "content",
            # "image" 
        ]
        #exclude = ['user']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Cannot be ABC")
        return content
    
       