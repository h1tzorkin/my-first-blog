from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^q$', views.list_2, name='list_2'),
    url(r'^light', views.list_3, name='list_3')
]
