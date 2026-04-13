from django.contrib import admin
from .models import Patient, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'blood_group', 'created_at')
    search_fields = ('name', 'contact_number')
    list_filter = ('gender', 'blood_group')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor_name', 'appointment_date', 'status')
    search_fields = ('doctor_name',)
    list_filter = ('status', 'appointment_date')

# Register your models here.
