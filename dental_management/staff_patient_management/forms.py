from django import forms
from .models import Clinic, Doctor, Patient, Appointment, DoctorClinicAffiliation

PROCEDURES = [
    ('Cleaning', 'Cleaning'),
    ('Filling', 'Filling'),
    ('Root Canal', 'Root Canal'),
    ('Crown', 'Crown'),
    ('Teeth Whitening', 'Teeth Whitening')
]

class DoctorForm(forms.ModelForm):
    specialties = forms.MultipleChoiceField(
        choices=PROCEDURES, 
        widget=forms.CheckboxSelectMultiple,  # Allow multiple selections
        required=False
    )

    class Meta:
        model = Doctor
        fields = ['npi', 'name', 'phone_number', 'email', 'specialties']

    def save(self, commit=True):
        instance = super().save(commit=False)
        # The form will return specialties as a list, so no need for conversion
        specialties = self.cleaned_data.get('specialties')
        instance.specialties = specialties  # Store directly as list in JSONField
        if commit:
            instance.save()
        return instance
        
        
# Clinic Form
class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'phone_number', 'email', 'address', 'city', 'state']

# Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'phone_number', 'email', 'address', 'clinic']

# Appointment Form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'clinic', 'appointment_date', 'procedures', 'doctor_notes']
        
# Doctor Affiliation Form
from django import forms
from .models import DoctorClinicAffiliation

class DoctorClinicAffiliationForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['doctor', 'office_address', 'day_of_week', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        clinic = kwargs.pop('clinic', None)  # Get the clinic instance passed
        super(DoctorClinicAffiliationForm, self).__init__(*args, **kwargs)

        if clinic:
            # Filter doctors to show only those not already affiliated with this clinic
            self.fields['doctor'].queryset = Doctor.objects.exclude(
                doctorclinicaffiliation__clinic=clinic
            )
        else:
            self.fields['doctor'].queryset = Doctor.objects.all()  # Fallback to all doctors

class AddDoctorAffiliationForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Select Doctor")
    office_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="Office Address")  # Adjusting rows to 3
    day_of_week = forms.CharField(max_length=10, label="Day of the Week")
    start_time = forms.TimeField(label="Start Time")
    end_time = forms.TimeField(label="End Time")
