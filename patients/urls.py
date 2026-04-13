from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    AppointmentViewSet,
    stats_view,
    upcoming_appointments,
    login_view
)

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', stats_view),
    path('appointments/upcoming/', upcoming_appointments),
    path('auth/login/', login_view),
]