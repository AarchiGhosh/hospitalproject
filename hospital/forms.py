from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from hospital.models import Doctor, Patient, User

class DoctorSignUpForm(UserCreationForm):
    specialisation = forms.CharField(max_length=10)
    department = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.specialisation = self.cleaned_data.get('specialisation')
        doctor.department = self.cleaned_data.get('department')
        return user


class PatientSignUpForm(UserCreationForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = False
        user.save()
        doctor = self.cleaned_data.get('doctor')
        patient = Patient.objects.create(user=user, doctor=doctor)
        return user

class PatientInfoForm:
    pass
