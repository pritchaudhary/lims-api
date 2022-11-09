from django.urls import path, include
from rest_framework import routers

from core_api.views import DepartmentsViews, DoctorViews, ParameterViews, SampleTypeViews, ServiceViews, SubDepartmentViews, TitleViews, DepartmentsByIdViews


router = routers.SimpleRouter()

urlpatterns = [
    path('department/', DepartmentsViews.as_view()),
    path('department/<str:pk>', DepartmentsByIdViews.as_view()),
    path('sub-department/', SubDepartmentViews.as_view()),
    path('sub-department/<str:pk>', SubDepartmentViews.as_view()),
    path('doctor/', DoctorViews.as_view()),
    path('doctor/<str:pk>', DoctorViews.as_view()),
    path('param/', ParameterViews.as_view()),
    path('param/<str:pk>', ParameterViews.as_view()),
    path('service/', ServiceViews.as_view()),
    path('service/<str:pk>', ServiceViews.as_view()),
    path('title/', TitleViews.as_view()),
    path('title/<str:pk>', TitleViews.as_view()),
    path('sample-type/', SampleTypeViews.as_view()),
    path('sample-type/<str:pk>', SampleTypeViews.as_view()),
]
