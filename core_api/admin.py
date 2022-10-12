from django.contrib import admin

from core_api.models import Departments, Doctor, Parameters, Sampletype, Service, SubDepartments, Titles

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
    list_display = ("full_name", "phone")
    search_fields = ["id", "full_name"]


@admin.register(Parameters)
class ParametersModel(admin.ModelAdmin):
    list_display = ("name", "report_name", "unit", "rate", "method", "suffix")
    search_fields = ["name", "report_name"]


@admin.register(Sampletype)
class SampletypeModel(admin.ModelAdmin):
    list_display = ("name", "sample_type", "description", "is_active")
    search_fields = ["name", "sample_type"]

@admin.register(Titles)
class TitleModel(admin.ModelAdmin):
    list_display = ("name", "gender", "dislay_order", "is_active")
    search_fields = ["name", "gender"]

@admin.register(Service)
class ServiceModel(admin.ModelAdmin):
    list_display = ("name", "report_name", "service_deptname", "rate", "method")
    search_fields = ["name", "report_name"]
