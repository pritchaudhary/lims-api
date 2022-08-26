from django.contrib import admin

from core_api.models import Departments, Doctor, SubDepartments

# Register your models here.


@admin.register(Departments)
class DepartmentsModel(admin.ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ["id", "name"]


@admin.register(SubDepartments)
class SubDepartmentsModel(admin.ModelAdmin):
    list_display = ("id", "name", "short_dep_name",
                    "barcode_print_flag", "departments")
    search_fields = ["id", "name", "departments__name"]
    # readonly_fields = ("guid",)
    list_filter = ["name", "short_dep_name", "barcode_print_flag", ]
    autocomplete_fields = ("departments",)


@admin.register(Doctor)
class DoctorModel(admin.ModelAdmin):
    list_display = ("doctor_name", "mobileno")
    search_fields = ["id", "doctor_name"]
