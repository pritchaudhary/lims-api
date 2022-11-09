from django.contrib import admin

from transactions.models import Patient, Visit

# Register your models here.

@admin.register(Patient)
class PatientModel(admin.ModelAdmin):
    list_display = ("patient_id", "title", "first_name", "middle_name", "last_name")
    search_fields = ["patient_id", "title","first_name", "middle_name", "last_name"]


@admin.register(Visit)
class VisitModel(admin.ModelAdmin):
    list_display = ("visit_id", "patient_id")
    search_fields = ["visit_id", "patient_id"]


