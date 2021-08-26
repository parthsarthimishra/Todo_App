from django import forms
from django import forms
from django.forms import widgets
from .models import TodoItem, TodoList
from django.forms import DateTimeInput

class datetime(forms.DateTimeInput):
    input_type = 'date'


class form_item(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title" , "checked" , "due_date"] 
        exclude=('todo_list',)
        widgets={"due_date": datetime()}



