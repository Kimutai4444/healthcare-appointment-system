from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
