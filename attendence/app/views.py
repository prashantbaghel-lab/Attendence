from django.shortcuts import render
from .serializer import Attendence_serializer, Courses_serializer, User_serializer, Departments_serializer, Students_serializer
from rest_framework.views import APIView
from .models import Attendence_log, Courses, Users, Departments, Student

from rest_framework import status, generics
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
#creation view for user Attendence_log_view


class Attendence_log_view(generics.CreateAPIView):

    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer

class cousre_vieW(generics.CreateAPIView):

    queryset=Courses.objects.all()
    serializer_class=Courses_serializer

class users_view(generics.CreateAPIView):

    queryset=Users.objects.all()
    serializer_class=User_serializer

class department_view(generics.CreateAPIView):

    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
class Student_view(generics.CreateAPIView):

    queryset=Student.objects.all()
    serializer_class=Students_serializer

class attendence_list_view(generics.ListAPIView):
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer

class course_list_view(generics.ListAPIView):
    queryset=Courses.objects.all()
    serializer_class=Courses_serializer

class user_list_view(generics.ListAPIView):
    queryset=Users.objects.all()
    serializer_class=User_serializer
class department_list_view(generics.ListAPIView):
    queryset=Departments.objects.all()
    serializer_class=Departments_serializer

class student_list_view(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=Students_serializer

class Attendence_log_Update_view(generics.UpdateAPIView):

    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    lookup_field="id"

class course__Update_view(generics.UpdateAPIView):

    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    lookup_field="id"

class users__Update_view(generics.UpdateAPIView):

    queryset=Users.objects.all()
    serializer_class=User_serializer
    lookup_field="id"

class department__Update_view(generics.UpdateAPIView):

    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    lookup_field="id"

class Student__Update_view(generics.UpdateAPIView):

    queryset=Student.objects.all()
    serializer_class=Students_serializer
    lookup_field="id"