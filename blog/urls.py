from django.conf.urls import url
from . import views

app_name='blog'

urlpatterns= [
    url('^$',views.post_list,name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$',views.post_details,name='post_details'),
    url(r'^new/$',views.post_new , name='post_new')
]