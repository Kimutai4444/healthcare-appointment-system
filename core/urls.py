from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare API",
        default_version='v1',
        description="API for managing appointments, doctors, and patients.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Patients and Doctors (make sure these are correct too)
    path('api/patients/', include('patients.urls')),
    path('api/doctors/',  include('doctors.urls')),

    # Appointments
    path('api/appointments/', include('appointments.urls')),

    # Token auth
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Swagger UIs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',  schema_view.with_ui('redoc',  cache_timeout=0), name='schema-redoc'),
]
