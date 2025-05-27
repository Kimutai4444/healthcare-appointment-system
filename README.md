# Healthcare Appointment Scheduling System

A Django REST Framework backend to manage patients, doctors, and appointment scheduling.

---

## Features

- **Patient Management**: Register, list, edit patient profiles  
- **Doctor Management**: Create and list doctor profiles and specializations  
- **Appointment Scheduling**: Book appointments with conflict checks (no past-date or double-booking; enforces doctor availability)  
- **Authentication**: Token-based (DRF `authtoken`)  
- **Documentation**: Swagger UI (`/swagger/`) and ReDoc (`/redoc/`)  
- **Filtering & Search** on list endpoints (`?search=`, `?filter=`, `?ordering=`)  
- **Pagination** (page size = 5 by default)  

---

## Quick Start

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Kimutai4444/healthcare-appointment-system.git
   cd healthcare-appointment-system
2. python -m venv env
```bash
  # Windows
  env\Scripts\activate
  # macOS / Linux
  source env/bin/activate
3. Install dependencies
```bash
  pip install -r requirements.txt
4. Run database migrations
```bash
  python manage.py migrate
5.Create a superuser (for admin and testing)
```bash
  python manage.py createsuperuser
6.Start the development server
  python manage.py runserver
7. Browse the API docs
  Swagger UI: http://127.0.0.1:8000/swagger/
  ReDoc: http://127.0.0.1:8000/redoc/

#AUTHENTICATION
  POST http://127.0.0.1:8000/api-token-auth/
  Content-Type: application/json
  
  {
    "username": "kimutai",
    "password": "cosmas@44"
  }
  Example Response
  json
  {
    "token": "43dca77ace84f995ffee2267f9cd070e1d4cff73"
  }
Use that token for all protected requests:
  Authorization: Token 43dca77ace84f995ffee2267f9cd070e1d4cff73

API Examples
  Create a Patient
  POST /api/patients/
  Authorization: Token 43dca77ace84f995ffee2267f9cd070e1d4cff73
  Content-Type: application/json
  
  {
    "full_name": "Jane Doe",
    "email": "jane@example.com",
    "phone_number": "0712345678",
    "national_id": "123456789",
    "insurance_number": "NHIF0001"
  }
List Doctors with Search & Ordering
  GET /api/doctors/?search=Smith&ordering=full_name
  Authorization: Token 43dca77ace84f995ffee2267f9cd070e1d4cff73

Book an Appointment
  POST /api/appointments/
  Authorization: Token 43dca77ace84f995ffee2267f9cd070e1d4cff73
  Content-Type: application/json
  
  {
    "patient": 1,
    "doctor": 2,
    "appointment_time": "2025-05-29T10:00:00Z",
    "status": "scheduled"
  }
Error Responses

  400 Bad Request – Validation errors
  
  json
  { "appointment_time": ["Appointment time must be in the future."] }
  400 Bad Request – Double-booking
  
  json
  { "non_field_errors": ["This doctor is already booked at that time."] }
  400 Bad Request – Outside availability
  
  json
  { "non_field_errors": ["Doctor is not available at this time."] }
  401 Unauthorized – Missing/invalid token
  
  json
  { "detail": "Authentication credentials were not provided." }
  404 Not Found – Invalid resource ID
  
  json
  { "detail": "Not found." }


Database Schema (ERD)
mermaid
erDiagram
    PATIENT ||--o{ APPOINTMENT : books
    DOCTOR  ||--o{ APPOINTMENT : receives

    PATIENT {
      int id PK
      string full_name
      string email
      string phone_number
      string national_id
      string insurance_number
    }

    DOCTOR {
      int id PK
      string full_name
      string email
      string specialization
    }

    APPOINTMENT {
      int id PK
      int patient_id FK
      int doctor_id FK
      datetime appointment_time
      string status
    }


Sequence Diagram (Booking Flow)
mermaid
sequenceDiagram
    Patient->>Frontend: Fill booking form
    Frontend->>Backend: POST /api/appointments/
    Backend->>DB: Check doctor availability & conflicts
    alt slot free
      Backend->>DB: Save appointment
      Backend-->>Frontend: 201 Created
    else conflict
      Backend-->>Frontend: 400 Bad Request
    end

Running Tests

  python manage.py test
  Deployment Notes
  Environment Variables:

  SECRET_KEY, DEBUG=False, DB credentials (DATABASE_URL), ALLOWED_HOSTS.

Production Server:

  Use Gunicorn/UWSGI behind Nginx, set DEBUG=False.
  
  Example Heroku Procfile:
  web: gunicorn core.wsgi --log-file -
  Static Files:
  
  Run python manage.py collectstatic and serve via CDN or Nginx.
  
  Security:
  
  Enforce HTTPS, secure cookies, HSTS (SECURE_HSTS_SECONDS)



Prepared by Cosmas Kimutai
