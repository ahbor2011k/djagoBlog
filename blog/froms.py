from django.forms import ModelForm
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from blog.models import Blog


class BlogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5 form-control","rows":6}, config_name="comment"
            )
        }

