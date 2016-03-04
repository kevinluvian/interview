from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^(?P<code>\w+)/$', views.queuelist, name='queuelist'),
	url(r'^(?P<code>\w+)/CALL/(?P<queuenum>\w+)/$', views.call, name='callqueue'),
	url(r'^(?P<code>\w+)/DELETE/(?P<queuenum>\w+)/$', views.delete, name='deletequeue'),
]