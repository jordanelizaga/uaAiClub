from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='projects'),
    url(r'^(?P<project_id>[0-9]+)/$', views.showProject, name='showProject'), #regex is hard
]