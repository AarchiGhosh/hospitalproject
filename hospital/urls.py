from django.urls import path
from hospital import views

urlpatterns = [
    path('',views.index, name = 'index'),
]