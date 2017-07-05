from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.verify, name='verify'),
    url(r'^confirmed/$', views.confirmed, name='confirmed'),
]
