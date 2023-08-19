from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('signup', views.signup, name='signup'),  # url something
    path('signin', views.signin, name='signin'),  # url for signin page
    path('logout', views.logout, name='logout')
]
