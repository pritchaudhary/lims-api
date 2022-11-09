from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from core_api.models import Departments, Doctor, Parameters, Sampletype, Service, SubDepartments, Titles
from django.http import Http404
from rest_framework import status
from core_api.serializers import DepartmentsSerializer, DoctorSerializer, ParameterSerializer, SampletypeSerializer, ServiceSerializer, SubDepartmentSerializer, TitleSerializer
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
            data = Departments.objects.get(pk = pk) #self.get_object(pk)
            serializer = DepartmentsSerializer(data, many=False)
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
    # permission_classes = (IsAuthenticated,)
    serializer_class = SubDepartmentSerializer

    def get_object(self, pk):
        try:
            return SubDepartments.objects.filter(pk=pk)
        except SubDepartments.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = SubDepartments.objects.get(pk = pk) #self.get_object(pk)
            serializer = SubDepartmentSerializer(data, many=False)
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
            data = Doctor.objects.get(pk = pk) #self.get_object(pk)
            serializer = DoctorSerializer(data, many=False)
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


class ParameterViews(APIView):
    serializer_class = ParameterSerializer

    def get_object(self, pk):
        try:
            return Parameters.objects.filter(pk=pk)
        except Parameters.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Parameters.objects.all()
        serializer = ParameterSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParameterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = Parameters.objects.get(pk=pk)
        serializer = ParameterSerializer(
            instance=data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            id = pk
            if not (id and Parameters.objects.filter(id=id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Parameters.objects.get(id=id)
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



class TitleViews(APIView):
    serializer_class = TitleSerializer

    def get_object(self, pk):
        try:
            return Titles.objects.filter(pk=pk)
        except Titles.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = Titles.objects.get(pk = pk) #self.get_object(pk)
            serializer = TitleSerializer(data, many=False)
        else:
            data = Titles.objects.all()
            serializer = TitleSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = Titles.objects.get(pk=pk)
        serializer = TitleSerializer(
            instance=data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            id = pk
            if not (id and Titles.objects.filter(id=id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Titles.objects.get(id=id)
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

class ServiceViews(APIView):
    serializer_class = ServiceSerializer

    def get_object(self, pk):
        try:
            return Parameters.objects.filter(pk=pk)
        except Parameters.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Service.objects.all()
        serializer = ServiceSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(
            instance=data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            id = pk
            if not (id and Service.objects.filter(id=id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Service.objects.get(id=id)
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


class SampleTypeViews(APIView):
    serializer_class = SampletypeSerializer

    def get_object(self, pk):
        try:
            return Sampletype.objects.filter(pk=pk)
        except Sampletype.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = Sampletype.objects.get(pk = pk) #self.get_object(pk)
            serializer = SampletypeSerializer(data, many=False)
        else:
            data = Sampletype.objects.all()
            serializer = SampletypeSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SampletypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = Sampletype.objects.get(pk=pk)
        serializer = SampletypeSerializer(
            instance=data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            id = pk
            if not (id and Sampletype.objects.filter(id=id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not record found")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Sampletype.objects.get(id=id)
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
