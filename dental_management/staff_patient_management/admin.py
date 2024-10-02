from datetime import timezone
from django.contrib import admin
from .models import Clinic, Doctor, Patient, Appointment

from django.contrib.auth.models import Group, User


admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Patient)