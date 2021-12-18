from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.generic import CreateView
from hospital.forms import PatientSignUpForm,DoctorSignUpForm
from hospital.models import User

def index(request):
    return render(request, 'hospital/base.html')

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'hospital/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(request, 'hospital/layout.html')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'hospital/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(request, 'hospital/layout.html')
