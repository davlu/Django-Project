'url pattern for learning_logs'

from django.conf.urls import url
from . import views
urlpatterns = [
    #home page
    url(r'^$',views.index, name = 'index'),
    url(r'^topics/$', views.topics , name = 'topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    url(r'^new_topic/$', views.new_url,name='new_topic'),
]

'''
url module allows for a request to be regex matched against the possible url's in urlpatterns.
'''