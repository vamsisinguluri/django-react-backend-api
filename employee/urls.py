from django.urls import path
from .views import *


urlpatterns = [

    path('api',EmployeeApi.as_view()),
    path('api/create',EmployeeCreateApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),
]