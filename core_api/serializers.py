from rest_framework import serializers
from .models import Departments, Doctor, Parameters, SubDepartments


class DepartmentsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True, initial=True)

    class Meta:
        model = Departments
        fields = ('__all__')


class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartments
        fields = ('__all__')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = ('__all__')
