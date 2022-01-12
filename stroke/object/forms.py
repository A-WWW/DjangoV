from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category not selected"

    class Meta:
        model = Object
        fields = ['title', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 15}),
        }

    # собственный валидатор
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            from django.core.exceptions import ValidationError
            raise ValidationError('Too long message(no more than 100 characters)')
        return title
