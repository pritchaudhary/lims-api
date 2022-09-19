from rest_framework import serializers
from .models import Departments, Doctor, Parameters, Sampletype, Service, SubDepartments, Titles


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


class SampletypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sampletype
        fields = ('__all__')


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('__all__')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')