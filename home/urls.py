from django.urls import path,include
from . import views



urlpatterns=[
    path('',views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('send_updates', views.send_updates, name='send_updates'),
]