from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newpost', views.newpost, name='newpost'),
    path('post/<str:pk>', views.post, name = 'post')
]