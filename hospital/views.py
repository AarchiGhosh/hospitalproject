from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from hospital.models import Bed, Service, User,Patient
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView
from hospital.forms import PatientSignUpForm, DoctorSignUpForm
from hospital.decorators import doctor_required

def index(request):
    header="Patient Tracking System"
    return render(request, 'hospital/index.html', {'header': header})

def contact(request):
    return render(request, 'hospital/contact.html')

def about(request):
    return render(request, 'hospital/about.html')


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, 'hospital/index.html')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, 'hospital/index.html')

@method_decorator([login_required, doctor_required], name='dispatch')
class PatientListView(ListView):
    model = Patient
    ordering = ('name', )
    context_object_name = 'patients'
    template_name = 'hospital/patient_list.html'

    def get_queryset(self):
        doctor = self.request.user.doctor
        queryset = Patient.objects.filter(doctor=doctor)
        return queryset


class AvailableServiceListView(ListView):
    model = Service
    ordering = ('service_name', )
    context_object_name = 'services'
    template_name = 'hospital/aservice_list.html'

    def get_queryset(self):   
        queryset = Service.objects.filter(is_available=True)
        return queryset

class CriticalServiceListView(ListView):
    model = Service
    ordering = ('service_name', )
    context_object_name = 'services'
    template_name = 'hospital/cservice_list.html'

    def get_queryset(self):   
        queryset = Service.objects.filter(is_critical=True)
        return queryset

class BedListView(ListView):
    model = Bed
    ordering = ('bed_number', )
    context_object_name = 'beds'
    template_name = 'hospital/bed_list.html'

    def get_queryset(self):   
        queryset = Bed.objects.filter(is_available=True)
        return queryset
