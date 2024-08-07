from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "is_important"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-3", "rows": 4}),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input mb-3"})
        }
