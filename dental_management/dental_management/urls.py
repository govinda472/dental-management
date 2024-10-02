"""
URL configuration for dental_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# dental_management/urls.py
# dental_management/urls.py

from django.contrib import admin
from django.urls import path, include
from staff_patient_management.views import RegularLoginView, dashboard_view
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def redirect_to_dashboard(request):
    return redirect('dashboard') 

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('login/', RegularLoginView.as_view(), name='login'),  # Regular login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in logout
    path('dashboard/', dashboard_view, name='dashboard'),  # Dashboard view

    # Include the URLs from the staff_patient_management app (which will handle clinics)
    path('management/', include('staff_patient_management.urls')),  # Point to app-level URLs
     path('', redirect_to_dashboard)
]
