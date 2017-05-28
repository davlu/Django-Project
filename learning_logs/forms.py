from django import forms
from .models import Topic
class topicForm(forms.modelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

