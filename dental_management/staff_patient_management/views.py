from asyncio.log import logger
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic, Doctor, Patient
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Clinic, Specialty
from .forms import ClinicForm, DoctorForm, PatientForm, AppointmentForm, DoctorClinicAffiliationForm


PROCEDURES = [
    ('Cleaning', 'Cleaning'),
    ('Filling', 'Filling'),
    ('Root Canal', 'Root Canal'),
    ('Crown', 'Crown'),
    ('Teeth Whitening', 'Teeth Whitening')
]

# Login view
class RegularLoginView(LoginView):
    template_name = 'login.html'  # Custom template for regular login

# Dashboard view
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Clinic List View
@login_required
def clinic_list_view(request):
    """
    View for listing clinics.
    """
    clinics = Clinic.objects.all()
    context = {'clinics': clinics}
    return render(request, 'clinic_list.html', context)


# Add/Edit Clinic View

# Add/Edit Clinic View (handles both regular form submission and JSON requests)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_clinic_view(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ClinicForm()
        return render(request, 'add_clinic.html', {'form': form})
# Edit Clinic View
@login_required
def edit_clinic_view(request, id):
    """
    View for editing an existing clinic.
    """
    clinic = get_object_or_404(Clinic, id=id)

    if request.method == 'POST':
        clinic.name = request.POST.get('name')
        clinic.phone_number = request.POST.get('phone_number')
        clinic.address = request.POST.get('address')
        clinic.city = request.POST.get('city')
        clinic.state = request.POST.get('state')
        clinic.save()

        return redirect('clinic_detail', id=clinic.id)

    return render(request, 'edit_clinic.html', {'clinic': clinic})

# Delete Clinic View
@login_required
def delete_clinic_view(request, id):
    """
    View for deleting a clinic.
    """
    clinic = get_object_or_404(Clinic, id=id)
    clinic.delete()
    return redirect('clinic_list')

@login_required
def add_patient_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = Patient.objects.create(
            name=data['name'],
            date_of_birth=data['date_of_birth'],
            phone_number=data['phone_number'],
            address=data['address'],
            ssn_last_4=data['ssn_last_4'],
            gender=data['gender']
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


# Doctor views

# Doctor List View
@login_required
def doctor_list_view(request):
    """
    View for listing doctors.
    """
    doctors = Doctor.objects.all()
    specialties = PROCEDURES  # Get all specialties to populate the dropdown
    context = {
        'doctors': doctors,
        'specialties': specialties,
    }
    return render(request, 'doctor_list.html', context)

# Doctor Detail View
@login_required
def doctor_detail_view(request, id):
    """
    View for showing doctor details.
    """
    doctor = get_object_or_404(Doctor, id=id)
    context = {'doctor': doctor}
    return render(request, 'doctor_detail.html', context)

# Add Doctor View
@login_required
def add_doctor_view(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()  # The save method will handle saving the specialties as a list
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})


# Edit Doctor View
#@login_required
#def edit_doctor_view(request, id):
    """
    View for editing an existing doctor.
    """
#    doctor = get_object_or_404(Doctor, id=id)

    #if request.method == 'POST':
        #doctor.name = request.POST.get('name')
        #doctor.npi = request.POST.get('npi')
        #doctor.phone_number = request.POST.get('phone_number')
        #doctor.email = request.POST.get('email')
        #doctor.specialties = request.POST.get('specialties')
        #doctor.save()

        #return redirect('doctor_detail', id=doctor.id)

    #return render(request, 'edit_doctor.html', {'doctor': doctor})

# Delete Doctor View
@login_required
def delete_doctor_view(request, id):
    """
    View for deleting a doctor.
    """
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('doctor_list')



# Patient List View
@login_required
def patient_list_view(request):
    """
    View for listing patients.
    """
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient_list.html', context)

# Patient Detail View
@login_required
def patient_detail_view(request, id):
    """
    View for showing patient details.
    """
    patient = get_object_or_404(Patient, id=id)
    context = {'patient': patient}
    return render(request, 'patient_detail.html', context)

# Add Patient View
@login_required
def add_patient_view(request):
    """
    View for adding a new patient.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = Patient.objects.create(
            name=data['name'],
            date_of_birth=data['date_of_birth'],
            phone_number=data['phone_number'],
            address=data['address'],
            ssn_last_4=data['ssn_last_4'],
            gender=data['gender']
        )
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# Edit Patient View
@login_required
def edit_patient_view(request, id):
    """
    View for editing an existing patient.
    """
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.date_of_birth = request.POST.get('date_of_birth')
        patient.phone_number = request.POST.get('phone_number')
        patient.address = request.POST.get('address')
        patient.ssn_last_4 = request.POST.get('ssn_last_4')
        patient.gender = request.POST.get('gender')
        patient.save()

        return redirect('patient_detail', id=patient.id)

    return render(request, 'edit_patient.html', {'patient': patient})

# Delete Patient View
@login_required
def delete_patient_view(request, id):
    """
    View for deleting a patient.
    """
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')

from .models import Doctor, DoctorSchedule
from django.http import HttpResponseRedirect




from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, DoctorClinicAffiliation
from .forms import DoctorForm

@login_required
def edit_doctor_view(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_detail', id=doctor.id)
    else:
        form = DoctorForm(instance=doctor)
    specialties = Specialty.objects.all()
    return render(request, 'edit_doctor.html', {'form': form, 'doctor': doctor, 'specialties': specialties})



from django.shortcuts import render, get_object_or_404, redirect
from .models import DoctorClinicAffiliation, Clinic, Doctor

@login_required
def edit_doctor_affiliation_view(request, doctor_id, clinic_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    clinic = get_object_or_404(Clinic, id=clinic_id)
    
    # Get the existing affiliation or create a new one
    affiliation = get_object_or_404(DoctorClinicAffiliation, doctor=doctor, clinic=clinic)

    if request.method == 'POST':
        form = DoctorClinicAffiliationForm(request.POST, instance=affiliation)
        if form.is_valid():
            form.save()
            return redirect('clinic_detail', id=clinic.id)
    else:
        form = DoctorClinicAffiliationForm(instance=affiliation)
    
    return render(request, 'edit_doctor_affiliation.html', {
        'form': form,
        'doctor': doctor,
        'clinic': clinic,
    })
from django import forms
class AddDoctorAffiliationForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Select Doctor")
    office_address = forms.CharField(widget=forms.Textarea, label="Office Address")
    day_of_week = forms.CharField(max_length=10, label="Day of the Week")
    start_time = forms.TimeField(label="Start Time")
    end_time = forms.TimeField(label="End Time")


@login_required
def clinic_detail_view(request, id):
    """
    View for showing clinic details and allowing clinic info edits and doctor affiliations.
    """
    clinic = get_object_or_404(Clinic, id=id)
    if request.method == 'GET':
        clinic_data = {
            'id': clinic.id,
            'name': clinic.name,
            'phone_number': clinic.phone_number,
            'email': clinic.email,
            'city': clinic.city,
            'state': clinic.state,
            'address': clinic.address,
        }
        return JsonResponse({'clinic': clinic_data})
    
    if request.method == 'POST':
        form = AddDoctorAffiliationForm(request.POST) 
        if form.is_valid():
            # Create a new DoctorClinicAffiliation
            DoctorClinicAffiliation.objects.create(
                clinic=clinic,
                doctor=form.cleaned_data['doctor'],
                office_address=form.cleaned_data['office_address'],
                day_of_week=form.cleaned_data['day_of_week'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
            )
            return redirect('clinic_detail', id=clinic.id)  # Redirect to avoid form re-submission
    else:
        form = AddDoctorAffiliationForm()

    context = {
        'clinic': clinic,
        'form': form,
    }

    return render(request, 'clinic_detail.html', context)


from .models import Clinic, DoctorClinicAffiliation





@login_required
def edit_doctor_affiliation_view(request, clinic_id, doctor_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    affiliation = get_object_or_404(DoctorClinicAffiliation, doctor_id=doctor_id, clinic=clinic)

    if request.method == 'POST':
        form = DoctorClinicAffiliationForm(request.POST, instance=affiliation)
        if form.is_valid():
            form.save()
            return redirect('clinic_detail', clinic_id=clinic.id)
    else:
        form = DoctorClinicAffiliationForm(instance=affiliation)

    return render(request, 'edit_doctor_affiliation.html', {'form': form, 'clinic': clinic, 'doctor': affiliation.doctor})


@login_required
def remove_doctor_affiliation_view(request, clinic_id, doctor_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    affiliation = get_object_or_404(DoctorClinicAffiliation, doctor_id=doctor_id, clinic=clinic)

    if request.method == 'POST':
        affiliation.delete()
        return redirect('clinic_detail', clinic_id=clinic.id)


def get_all_doctors(request):
    doctors = Doctor.objects.all()
    doctor_list = [{"id": doctor.id, "name": doctor.name} for doctor in doctors]
    return JsonResponse({'doctors': doctor_list})

#@login_required
@csrf_exempt
def add_doctor_affiliation_view(request, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)

    if request.method == 'POST':
        form = DoctorClinicAffiliationForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('clinic_detail', clinic_id=clinic_id)
    else:
        form = DoctorClinicAffiliationForm()

    return render(request, 'add_doctor_affiliation.html', {'form': form, 'clinic': clinic})
