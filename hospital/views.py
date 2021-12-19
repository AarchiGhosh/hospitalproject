from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from hospital.models import User
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from hospital.forms import PatientSignUpForm, DoctorSignUpForm

def index(request):
    return render(request, 'hospital/base.html')

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
