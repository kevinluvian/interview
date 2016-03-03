from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.group, name='choosegroup'),
    url(r'^(?P<group>\w+)/$', views.department, name='choosedepartment'),
]