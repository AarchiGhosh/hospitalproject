from django.urls import path
from hospital import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/available/', views.AvailableServiceListView.as_view(), name='aservice_list'),
    path('services/critical/', views.CriticalServiceListView.as_view(), name='cservice_list'),
    path('services/beds/', views.BedListView.as_view(), name='bed_list'),
]