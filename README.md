# Bright Smile Dental Management

Bright Smile Dental Management is a Django-based platform for managing clinics, doctors, patients, and their affiliations, built to streamline dental management workflows.

## Features
- **Add, Edit, and Delete Clinics**: Manage clinic details including name, address, and contact information.
- **Add, Edit, and Delete Doctors**: Manage doctor information such as NPI, specialties, and contact details.
- **Add, Edit, and Delete Patients**: Handle patient information like name, date of birth, contact details, and affiliated clinic.
- **Doctor-Clinic Affiliation**: Link doctors to clinics with office addresses and working schedules.
- **REST API Support**: Expose endpoints to interact with external systems.

## REST API Endpoints

The platform exposes a few REST API functionalities to allow external systems to perform the following operations via API calls:

- **Add Patient** (no affiliation required)
- **Add Doctor** (no affiliation required)
- **Add Clinic** (no affiliation required)
- **Get Clinic Information** (without affiliated patients and doctors)

### REST Endpoints:
- base link http://127.0.0.1:8000/
- **Add Clinic**: `/clinics/add/` [POST]
- **Add Doctor**: `/doctors/add/` [POST]
- **Add Patient**: `/patients/add/` [POST]
- **Get Clinic Information**: `/clinics/<clinic_id>/` [GET]

## Project Setup Instructions

To set up and run the project locally, follow these steps:

### Prerequisites
- Python 3.x
- Virtual environment (optional but recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/govinda472/bright-smile-dental-management.git

### 2. Navigate to the Project Directory

cd bright-smile-dental-management

### 3. Set Up a Virtual Environment 

python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


### 4. Run the Django Development Server

python manage.py runserver


### 5. Access the Application

http://127.0.0.1:8000/admin/


Username: admin
Password: 12345678


