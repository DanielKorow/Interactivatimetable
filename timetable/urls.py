from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^login/', views.authorizationband, name="auth"),
    url(r'^schedule/', views.schedule, name="schedule"),
    url(r'^create/', views.create_rep, name="create"),
]
