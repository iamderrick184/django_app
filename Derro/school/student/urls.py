from django.urls import path
from . import views

urlpatterns=[
    path('',views.app_index),
    path('bob',views.app_info),
]