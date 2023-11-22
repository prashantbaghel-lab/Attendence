from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .serializer import Attendence_serializer, User_serializer, Departments_serializer, Students_serializer, Courses_serializer
from rest_framework.views import APIView
from .models import Attendence_log, Courses, Users, Departments, Student
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from django.http import HttpResponse
from rest_framework.response import Response
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")
# Create your views here.


#creation view for user Attendence_log_view
class Attendence_log_view(generics.CreateAPIView):
    #permission_classes=[IsAuthenticated]
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    logger.info("Attendence log view create")
    def create(self, request, *args, **kwargs):
        try:
            # Call the create method from CreateAPIView
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# view for Course Creation
class cousre_vieW(generics.CreateAPIView):

    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    logger.info("New Course  Create")
    def create(self, request, *args, **kwargs):
        try:
            # Call the create method from CreateAPIView
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
#view for User Creation
class users_view(generics.CreateAPIView):

    queryset=Users.objects.all()
    serializer_class=User_serializer
    logger.info("New User Create")
    def create(self, request, *args, **kwargs):
        try:
            # Call the create method from CreateAPIView
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

#view for Departments Creation
class department_view(generics.CreateAPIView):

    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    logger.info("New Department Create")
    def create(self, request, *args, **kwargs):
        try:
            # Call the create method from CreateAPIView
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

#view for Student Creation      
class Student_view(generics.CreateAPIView):

    queryset=Student.objects.all()
    serializer_class=Students_serializer
    logger.info("New Student create")
    def create(self, request, *args, **kwargs):
        try:
            # Call the create method from CreateAPIView
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

#list the attendence log
class attendence_list_view(generics.ListAPIView):
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    logger.info("Attendence log list")
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Check if the queryset is empty
            if not queryset.exists():
                return Response(
                    {"error": "No data available."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Call the list method from ListAPIView
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

#list the Course 
class course_list_view(generics.ListAPIView):
    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    logger.info("Course List ")
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Check if the queryset is empty
            if not queryset.exists():
                return Response(
                    {"error": "No data available."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Call the list method from ListAPIView
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

#list the User 
class user_list_view(generics.ListAPIView):
    queryset=Users.objects.all()
    serializer_class=User_serializer
    logger.info("User List ")
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Check if the queryset is empty
            if not queryset.exists():
                return Response(
                    {"error": "No data available."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Call the list method from ListAPIView
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

#list the Departments
class department_list_view(generics.ListAPIView):
    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    logger.info("Department List ")
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Check if the queryset is empty
            if not queryset.exists():
                return Response(
                    {"error": "No data available."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Call the list method from ListAPIView
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
#list the Student
class student_list_view(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=Students_serializer
    logger.info("Student List ")
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            
            # Check if the queryset is empty
            if not queryset.exists():
                return Response(
                    {"error": "No data available."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Call the list method from ListAPIView
            response = super().list(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

#update the Attendence log by id
class Attendence_log_Update_view(generics.UpdateAPIView):

    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    lookup_field="id"
    logger.info(f"Attendence log with this is {lookup_field} update ")
    
#Update the Cousre by Id
class course__Update_view(generics.UpdateAPIView):

    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    lookup_field="id"
    logger.info(f"Course  with this is {lookup_field} update ")


#Update the User by Id
class users__Update_view(generics.UpdateAPIView):

    queryset=Users.objects.all()
    serializer_class=User_serializer
    lookup_field="id"
    logger.info(f"User  with this is {lookup_field} update ")

#update the Departments By id 
class department__Update_view(generics.UpdateAPIView):

    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    lookup_field="id"

#update the Student By id 
class Student__Update_view(generics.UpdateAPIView):

    queryset=Student.objects.all()
    serializer_class=Students_serializer
    lookup_field="id"