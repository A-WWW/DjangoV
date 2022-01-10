from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), required=False)
    is_published = forms.BooleanField(initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Category not selected")