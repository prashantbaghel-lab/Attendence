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
from django.http import Http404
from rest_framework.response import Response
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")
# Create your views here.


#creation view for user Attendence_log_view
class Attendence_log_view(generics.CreateAPIView):
    """
    API view for creating attendance logs.
    - Handles the creation of new attendance logs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Attendence_log model.
        serializer_class (Serializer): Serializer class for the Attendence_log model.
    """
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    logger.info("Attendence log view create")
    def create(self, request, *args, **kwargs):
        """
        Create a new attendance log.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Exception: If an error occurs during the creation process.
        """
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
    """
    API view for creating new courses.

    - Handles the creation of new courses.

    Attributes:
        queryset (QuerySet): Includes all objects from the Courses model.
        serializer_class (Serializer): Serializer class for the Courses model.
    """
    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    logger.info("New Course  Create")
    def create(self, request, *args, **kwargs):
        """
        Create a new course.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Exception: If an error occurs during the creation process.
        """
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
    """
    API view for creating new users.

    - Handles the creation of new users.

    Attributes:
        queryset (QuerySet): Includes all objects from the Courses users.
        serializer_class (Serializer): Serializer class for the Courses users.
    """
    queryset=Users.objects.all()
    serializer_class=User_serializer
    logger.info("New User Create")
    def create(self, request, *args, **kwargs):
        """
        Create a new user.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Exception: If an error occurs during the creation process.
        """
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
    """
    API view for creating new departments.

    - Handles the creation of new departments.

    Attributes:
        queryset (QuerySet): Includes all objects from the Departments model.
        serializer_class (Serializer): Serializer class for the Departments model.
    """
    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    logger.info("New Department Create")
    def create(self, request, *args, **kwargs):
        """
        Create a new department.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Exception: If an error occurs during the creation process.
        """
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
    """
    API view for creating new Students.

    - Handles the creation of new Students.

    Attributes:
        queryset (QuerySet): Includes all objects from the Students model.
        serializer_class (Serializer): Serializer class for the Students model.
    """

    queryset=Student.objects.all()
    serializer_class=Students_serializer
    logger.info("New Student create")
    def create(self, request, *args, **kwargs):
        """
        Create a new Student.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Exception: If an error occurs during the creation process.
        """
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
    """
    API view for listing attendance logs.

    - Retrieves and lists attendance logs.
    - Handles cases where no data is available or an error occurs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Attendence_log model.
        serializer_class (Serializer): Serializer class for the Attendence_log model.
    """
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    logger.info("Attendence log list")
    def list(self, request, *args, **kwargs):
        """
        List attendance logs.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response containing the list of attendance logs.

        Raises:
            Response with status code 404 (Not Found): If no data is available.
            Response with status code 500 (Internal Server Error): If an error occurs.
        """
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
    """
    API view for listing courses.

    - Retrieves and lists courses.
    - Handles cases where no data is available or an error occurs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Courses model.
        serializer_class (Serializer): Serializer class for the Courses model.
    """
    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    logger.info("Course List ")
    def list(self, request, *args, **kwargs):
        """
        List courses.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response containing the list of courses.

        Raises:
            Response with status code 404 (Not Found): If no data is available.
            Response with status code 500 (Internal Server Error): If an error occurs.
        """
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
    """
    API view for listing users.

    - Retrieves and lists users.
    - Handles cases where no data is available or an error occurs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Users model.
        serializer_class (Serializer): Serializer class for the Users model.
    """

    queryset=Users.objects.all()
    serializer_class=User_serializer
    logger.info("User List ")
    def list(self, request, *args, **kwargs):
        """
        List users.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response containing the list of users.

        Raises:
            Response with status code 404 (Not Found): If no data is available.
            Response with status code 500 (Internal Server Error): If an error occurs.
        """
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
    """
    API view for listing departments.

    - Retrieves and lists departments.
    - Handles cases where no data is available or an error occurs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Departments model.
        serializer_class (Serializer): Serializer class for the Departments model.
    """
    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    logger.info("Department List ")
    def list(self, request, *args, **kwargs):
        """
        List departments.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response containing the list of departments.

        Raises:
            Response with status code 404 (Not Found): If no data is available.
            Response with status code 500 (Internal Server Error): If an error occurs.
        """
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
    """
    API view for listing students.

    - Retrieves and lists students.
    - Handles cases where no data is available or an error occurs.

    Attributes:
        queryset (QuerySet): Includes all objects from the Student model.
        serializer_class (Serializer): Serializer class for the Student model.
    """
    queryset=Student.objects.all()
    serializer_class=Students_serializer
    logger.info("Student List ")
    def list(self, request, *args, **kwargs):
        """
        List students.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response containing the list of students.

        Raises:
            Response with status code 404 (Not Found): If no data is available.
            Response with status code 500 (Internal Server Error): If an error occurs.
        """
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
    """
    API view for updating an existing attendance log.

    - Handles the update of an attendance log based on the provided 'id'.
    - Uses the 'id' as the lookup field.
    - Logs the update action.

    Attributes:
        queryset (QuerySet): Includes all objects from the Attendence_log model.
        serializer_class (Serializer): Serializer class for the Attendence_log model.
        lookup_field (str): Field used for looking up the attendance log (set to 'id').
    """
    queryset=Attendence_log.objects.all()
    serializer_class=Attendence_serializer
    lookup_field="id"
    logger.info(f"Attendence log with this is {lookup_field} update ")
    def update(self, request, *args, **kwargs):
        """
        Update an existing attendance log.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Response with status code 404 (Not Found): If the attendance log is not found.
            Response with status code 500 (Internal Server Error): If an error occurs during the update.
        """
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Http404:
            return Response({"error": "Attendence log not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating Attendence log: {str(e)}")
            return Response({"error": "An error occurred during the update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#Update the Cousre by Id
class course__Update_view(generics.UpdateAPIView):
    """
    API view for updating an existing course.

    - Handles the update of a course based on the provided 'id'.
    - Uses the 'id' as the lookup field.
    - Logs the update action.

    Attributes:
        queryset (QuerySet): Includes all objects from the Courses model.
        serializer_class (Serializer): Serializer class for the Courses model.
        lookup_field (str): Field used for looking up the course (set to 'id').
    """
    queryset=Courses.objects.all()
    serializer_class=Courses_serializer
    lookup_field="id"
    logger.info(f"Course  with this is {lookup_field} update ")
    def update(self, request, *args, **kwargs):
        """
        Update an existing course.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Response with status code 404 (Not Found): If the course is not found.
            Response with status code 500 (Internal Server Error): If an error occurs during the update.
        """
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Http404:
            return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating Course: {str(e)}")
            return Response({"error": "An error occurred during the update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


#Update the User by Id
class users__Update_view(generics.UpdateAPIView):
    """
    API view for updating an existing user.

    - Handles the update of a user based on the provided 'id'.
    - Uses the 'id' as the lookup field.
    - Logs the update action.

    Attributes:
        queryset (QuerySet): Includes all objects from the Users model.
        serializer_class (Serializer): Serializer class for the Users model.
        lookup_field (str): Field used for looking up the user (set to 'id').
    """
    queryset=Users.objects.all()
    serializer_class=User_serializer
    lookup_field="id"
    logger.info(f"User  with this is {lookup_field} update ")
    def update(self, request, *args, **kwargs):
        """
        Update an existing user.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Response with status code 404 (Not Found): If the user is not found.
            Response with status code 500 (Internal Server Error): If an error occurs during the update.
        """
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Http404:
            return Response({"error": "Users not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating Users: {str(e)}")
            return Response({"error": "An error occurred during the update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



#update the Departments By id 
class department__Update_view(generics.UpdateAPIView):
    """
    API view for updating an existing department.

    - Handles the update of a department based on the provided 'id'.
    - Uses the 'id' as the lookup field.
    - Logs the update action.

    Attributes:
        queryset (QuerySet): Includes all objects from the Departments model.
        serializer_class (Serializer): Serializer class for the Departments model.
        lookup_field (str): Field used for looking up the department (set to 'id').
    """
    queryset=Departments.objects.all()
    serializer_class=Departments_serializer
    lookup_field="id"
    def update(self, request, *args, **kwargs):
        """
        Update an existing department.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Response with status code 404 (Not Found): If the department is not found.
            Response with status code 500 (Internal Server Error): If an error occurs during the update.
        """
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Http404:
            return Response({"error": "Departments not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating Departments: {str(e)}")
            return Response({"error": "An error occurred during the update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#update the Student By id 
class Student__Update_view(generics.UpdateAPIView):
    """
    API view for updating an existing student.

    - Handles the update of a student based on the provided 'id'.
    - Uses the 'id' as the lookup field.
    - Logs the update action.

    Attributes:
        queryset (QuerySet): Includes all objects from the Student model.
        serializer_class (Serializer): Serializer class for the Student model.
        lookup_field (str): Field used for looking up the student (set to 'id').
    """
    queryset=Student.objects.all()
    serializer_class=Students_serializer
    lookup_field="id"
    def update(self, request, *args, **kwargs):
        """
        Update an existing student.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            Response with status code 404 (Not Found): If the student is not found.
            Response with status code 500 (Internal Server Error): If an error occurs during the update.
        """
        try:
            response = super().update(request, *args, **kwargs)
            return response
        except Http404:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error updating Student: {str(e)}")
            return Response({"error": "An error occurred during the update."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
