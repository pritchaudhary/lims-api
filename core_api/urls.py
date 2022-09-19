from django.urls import path, include
from rest_framework import routers

from core_api.views import DepartmentsViews, DoctorViews, ParameterViews, ServiceViews, SubDepartmentViews


router = routers.SimpleRouter()

urlpatterns = [
    path('department/', DepartmentsViews.as_view()),
    path('department/<str:pk>', DepartmentsViews.as_view()),
    path('sub-department/', SubDepartmentViews.as_view()),
    path('sub-department/<str:pk>', SubDepartmentViews.as_view()),
    path('doctor/', DoctorViews.as_view()),
    path('doctor/<str:pk>', DoctorViews.as_view()),
    path('param/', ParameterViews.as_view()),
    path('param/<str:pk>', ParameterViews.as_view()),
    path('service/', ServiceViews.as_view()),
    path('service/<str:pk>', ServiceViews.as_view()),
]
