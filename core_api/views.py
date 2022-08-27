from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from core_api.models import Departments, Doctor, SubDepartments
from django.http import Http404
from rest_framework import status
from core_api.serializers import DepartmentsSerializer, DoctorSerializer, SubDepartmentSerializer
from accounts.helpers import response_dict
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView

# Create your views here.


class DepartmentsViews(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DepartmentsSerializer

    def get_object(self, pk):
        try:
            return Departments.objects.filter(pk=pk)
        except Departments.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Departments.objects.all()
        serializer = DepartmentsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        # department = Departments.objects.get(pk=pk)
        serializer = DepartmentsSerializer(
            instance=Departments.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            department_id = pk
            if not (department_id and Departments.objects.filter(id=department_id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Departments.objects.get(id=department_id)
                instance.delete()
                #### Below code for soft delete ##
                # instance.is_active = False
                # instance.save()
                response = response_dict(
                    data=dict(id=department_id), error=False, message="Successfully deleted.")
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = response_dict(
                data=None, error=True, message=str(e.__str__()))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class SubDepartmentViews(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubDepartmentSerializer

    def get_object(self, pk):
        try:
            return SubDepartments.objects.filter(pk=pk)
        except SubDepartments.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = SubDepartments.objects.all()
        serializer = SubDepartmentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        # department = Departments.objects.get(pk=pk)
        serializer = SubDepartmentSerializer(
            instance=SubDepartments.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            department_id = pk
            if not (department_id and SubDepartments.objects.filter(id=department_id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = SubDepartments.objects.get(id=department_id)
                instance.delete()
                #### Below code for soft delete ##
                # instance.is_active = False
                # instance.save()
                response = response_dict(
                    data=dict(id=department_id), error=False, message="Successfully deleted.")
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = response_dict(
                data=None, error=True, message=str(e.__str__()))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class DoctorViews(APIView):
    serializer_class = DoctorSerializer

    def get_object(self, pk):
        try:
            return Doctor.objects.filter(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Doctor.objects.all()
        serializer = DoctorSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(
            instance=data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            id = pk
            if not (id and Doctor.objects.filter(id=id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Doctor.objects.get(id=id)
                instance.delete()
                #### Below code for soft delete ##
                # instance.is_active = False
                # instance.save()
                response = response_dict(
                    data=dict(id=id), error=False, message="Successfully deleted.")
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = response_dict(
                data=None, error=True, message=str(e.__str__()))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
