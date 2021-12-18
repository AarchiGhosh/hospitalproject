from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from hospital.models import Doctor, Patient, User

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
        patient = Patient.objects.create(user=user)
        student.doctor = self.cleaned_data.get('doctor')
        return user

class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user
