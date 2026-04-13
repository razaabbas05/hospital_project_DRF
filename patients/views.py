from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrReadOnly


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        queryset = Patient.objects.all()
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset
    
class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        queryset = Appointment.objects.all()
        status = self.request.query_params.get('status')
        patient_id = self.request.query_params.get('patient_id')

        if status:
            queryset = queryset.filter(status=status)

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stats_view(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()

    status_counts = (
        Appointment.objects
        .values('status')
        .annotate(count=Count('status'))
    )

    return Response({
        "success": True,
        "data": {
            "total_patients": total_patients,
            "total_appointments": total_appointments,
            "appointments_by_status": list(status_counts)
        },
        "message": "Stats fetched successfully"
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upcoming_appointments(request):
    now = timezone.now()
    next_week = now + timedelta(days=7)

    appointments = Appointment.objects.filter(
        appointment_date__range=[now, next_week]
    ).order_by('appointment_date')

    serializer = AppointmentSerializer(appointments, many=True)
    return Response({
        "success": True,
        "data": serializer.data,
        "message": "Upcoming appointments fetched"
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "success": True,
            "data": {"token": token.key},
            "message": "Login successful"
        })

    return Response({
        "success": False,
        "data": None,
        "message": "Invalid credentials"
    }, status=400)
