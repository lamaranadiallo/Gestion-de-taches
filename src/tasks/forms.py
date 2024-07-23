from django import  forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date', 'completed','priority']
        widgets = {
            'due_date':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }