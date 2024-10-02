# staff_patient_management/urls.py

from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

     path('admin/', admin.site.urls),
   # Clinics
    path('clinics/', views.clinic_list_view, name='clinic_list'),
    path('clinics/add/', views.add_clinic_view, name='add_clinic'),
    path('clinics/<int:id>/', views.clinic_detail_view, name='clinic_detail'),
    path('clinics/<int:id>/edit/', views.edit_clinic_view, name='edit_clinic'),
    path('clinics/<int:id>/delete/', views.delete_clinic_view, name='delete_clinic'),
    path('clinics/<int:id>/', views.clinic_detail_view, name='clinic_detail'),  
    path('clinic/<int:clinic_id>/doctor/<int:doctor_id>/edit_affiliation/', views.edit_doctor_affiliation_view, name='edit_doctor_affiliation'),
    path('clinics/<int:clinic_id>/', views.clinic_detail_view, name='clinic_detail'),
    path('clinics/<int:clinic_id>/add_affiliation/', views.add_doctor_affiliation_view, name='add_doctor_affiliation'),
    path('clinics/<int:clinic_id>/doctor/<int:doctor_id>/edit_affiliation/', views.edit_doctor_affiliation_view, name='edit_doctor_affiliation'),
    path('clinics/<int:clinic_id>/doctor/<int:doctor_id>/remove_affiliation/', views.remove_doctor_affiliation_view, name='remove_doctor_affiliation'),
   
    #path('clinics/<int:id>/', get_clinic_detail_view, name='get_clinic_detail'),  
    path('get-all-doctors/', views.get_all_doctors, name='get_all_doctors'),
    
    path('doctors/', views.doctor_list_view, name='doctor_list'),  
    path('doctors/add/', views.add_doctor_view, name='add_doctor'),  
    path('doctors/<int:id>/', views.doctor_detail_view, name='doctor_detail'), 
    path('doctors/<int:id>/edit/', views.edit_doctor_view, name='edit_doctor'),  
    path('doctors/<int:id>/delete/', views.delete_doctor_view, name='delete_doctor'), 
    

      
    path('patients/', views.patient_list_view, name='patient_list'),  
    path('patients/add/', views.add_patient_view, name='add_patient'),  
    path('patients/<int:id>/', views.patient_detail_view, name='patient_detail'),  
    path('patients/<int:id>/edit/', views.edit_patient_view, name='edit_patient'),  
    path('patients/<int:id>/delete/', views.delete_patient_view, name='delete_patient'),  
]
    