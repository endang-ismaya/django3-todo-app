from django import forms
from django.forms import fields

from .models import SingleTodo


class SingleTodoForm(forms.ModelForm):
    class Meta:
        model = SingleTodo
        fields = ["title"]
