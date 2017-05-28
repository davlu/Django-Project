from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import topicForm

def index(request):
    return render(request, 'learning_logs/index.html')
'''
takes a request and returns main page for index.html
'''
def topics(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)
'''
Takes request and returns html link. Context dictionary can be used with instances of Topic available for use
within html document.
'''
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = Topic.entry_set.order_by('- date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)
'''
Takes a topic id argument and searches Topic instances for the object with that topic id.
returns context with dictionary keys and values available for contextual use within the html document.
'''

def new_topic(request):
    "supports the addition of new topics"
    if request.method != 'POST':
        form = topicForm()
    else:
        form = topicForm(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html')

# Create your views here.