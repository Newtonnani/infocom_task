from os import name
from django.urls import path
from . import views

app_name = 'sheets'

urlpatterns = [
    path('',views.index,name='index'),
    path('data/',views.data,name='data'),
    path('data_submit',views.data_submit,name='data_submit')
]
