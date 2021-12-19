from django.urls import path
from hospital import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
]