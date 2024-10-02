from django.db import models

# Predefined list of procedures (specialties)
PROCEDURES = [
    ('Cleaning', 'Cleaning'),
    ('Filling', 'Filling'),
    ('Root Canal', 'Root Canal'),
    ('Crown', 'Crown'),
    ('Teeth Whitening', 'Teeth Whitening')
]


class Specialty(models.Model):
    name = models.CharField(max_length=50, choices=PROCEDURES, unique=True)

    def __str__(self):
        return self.name
    
# Clinic Model
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

# Doctor Model
class Doctor(models.Model):
    npi = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    
    # Many-to-Many relationship with Specialties
    specialties = models.JSONField(default=list, blank=True)

    # Many-to-Many relationship with Clinics via DoctorClinicAffiliation
    clinics = models.ManyToManyField(Clinic, related_name="doctors", through='DoctorClinicAffiliation')
    
    def __str__(self):
        return self.name


# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    # Each patient is affiliated with one clinic
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, related_name="patients")

    def __str__(self):
        return self.name


# Appointment Model
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    # Specialties or procedures chosen from predefined choices
    procedures = models.CharField(max_length=20, choices=PROCEDURES)
    doctor_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.patient.name} ({self.appointment_date})"


# Doctor Schedule Model (for managing doctor schedules)
class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)  # e.g., 'Monday', 'Tuesday'
    start_time = models.TimeField()  # e.g., '09:00'
    end_time = models.TimeField()  # e.g., '17:00'

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week}: {self.start_time} to {self.end_time}"


# Doctor-Clinic Affiliation (many-to-many through model)
class DoctorClinicAffiliation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    office_address = models.TextField(default="none")
    day_of_week = models.CharField(max_length=10)  
    start_time = models.TimeField()  
    end_time = models.TimeField()  

    def __str__(self):
        return f"{self.doctor.name} - {self.clinic.name} Affiliation"
