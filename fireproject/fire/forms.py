from django import forms
from .models import *

class FireForm(forms.ModelForm):
    class Meta:
        model = Fire
        fields = ["title","content"]
        labels = {
            "title" : "제목",
            "content" : "내용"
        }