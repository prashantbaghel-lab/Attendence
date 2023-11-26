from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Attendence_log,Courses, Departments, Users, Student
from django.contrib.auth.models import User


class AttendenceLogViewTestCase(TestCase):
    """
    Test case for the AttendenceLogView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_create_attendence_log: Test creating an attendence log via API.
    """
    def setUp(self):
        """
        Set up the test case.

        - Initializes an API client for making requests.
        - Retrieves or creates a superuser for authentication purposes.
        """
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_attendence_log(self):
        """
        Test creating an attendence log via the API.

        - Defines the URL for creating attendence logs.
        - Defines the data for creating an attendence log.
        - Authenticates with the API using superuser credentials.
        - Sends a POST request to create an attendence log.
        - Prints request and response details for debugging.
        - Asserts that the status code is HTTP 201 Created.
        - Retrieves the created attendence log from the database.
        - Asserts that the attendence log attributes match the provided data.
        """
        url ='http://127.0.0.1:8000/api/attendence_log_create/'

        data = {
            "id":1,
            "Student_id":1,
            "course_id":1,
            "present":"Yes",
            "submitted_by":"student1"
            }

        
        client=self.client
        #authentication logic
        client.login(username="admin", password="123")
        print(f"Request headers: {self.client.headers}")
        response = self.client.post(url, data, format='json')
        print(f"Response headers: {response.headers}")
        print(f"Superuser credentials: {self.existing_superuser.username}:{self.existing_superuser.password}")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        attendence_log = Attendence_log.objects.get(id=1)
        self.assertEqual(attendence_log.Student_id, 1)
        self.assertEqual(attendence_log.course_id, 1)
        self.assertEqual(attendence_log.present, 'Yes')
        self.assertEqual(attendence_log.submitted_by, 'student1')


class CourseViewTestCase(TestCase):
    """
    Test case for the CourseView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_create_course: Test creating a course via API.
    """
    def setUp(self):
        """
        Set up the test case.

        - Initializes an API client for making requests.
        - Retrieves or creates a superuser for authentication purposes.
        """
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
        """
        Test creating a course via the API.

        - Creates an Attendence_log object for testing.
        - Defines the URL for creating courses.
        - Defines the data for creating a course.
        - Authenticates with the API using superuser credentials.
        - Sends a POST request to create a course.
        - Prints request and response details for debugging.
        - Asserts that the status code is HTTP 201 Created.
        - Retrieves the created course from the database.
        - Asserts that the course attributes match the provided data.
        """
        attendence_log = Attendence_log.objects.create(id=1, Student_id=1, course_id=1, present='Yes', submitted_by='student1')
        url ='http://127.0.0.1:8000/api/course_create/'

        data = {
            "id": 1,
            "course_name":"B.E",
            "department_id":1,
            "semester":"5th",
            "classs":"2nd",
            "lecture_hours":"1",
            "submitted_by":"student1"
        }

        
        client=self.client
        client.login(username="admin", password="123")
        print(f"Request headers: {self.client.headers}")
        response = self.client.post(url, data, format='json')
        print(f"Response headers: {response.headers}")
        print(f"Superuser credentials: {self.existing_superuser.username}:{self.existing_superuser.password}")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        courses = Courses.objects.get(id= data['id'])
        self.assertEqual(courses.course_name, "B.E")
        self.assertEqual(courses.department_id, 1)
        self.assertEqual(courses.semester, "5th")
        self.assertEqual(courses.classs, "2nd")
        self.assertEqual(courses.lecture_hours, '1')
        self.assertEqual(courses.submitted_by, 'student1')
        

class UserViewTestCase(TestCase):
    """
    Test case for the UserView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_create_user: Test creating a user via API.
    """
    def setUp(self):
        """
        Set up the test case.

        - Initializes an API client for making requests.
        - Retrieves or creates a superuser for authentication purposes.
        """
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
        """
        Test creating a user via the API.

        - Creates an Attendence_log object for testing.
        - Defines the URL for creating users.
        - Defines the data for creating a user.
        - Authenticates with the API using superuser credentials.
        - Sends a POST request to create a user.
        - Prints request and response details for debugging.
        - Asserts that the status code is HTTP 201 Created.
        - Retrieves the created user from the database.
        - Asserts that the user attributes match the provided data.
        """
        attendence_log = Attendence_log.objects.create(id=1, Student_id=1, course_id=1, present='Yes', submitted_by='student1')
        

        url ='http://127.0.0.1:8000/api/user_createe/'

        data = {
            "id":1,
            "type_user":"student",
            "full_name":"prashant Baghel",
            "username":"prashant",
            "email":"prashant@gmail.com",
            "password":"123",
            "submitted_by":"student1"
        }

        
        client=self.client
        client.login(username="admin", password="123")
        print(f"Request headers: {self.client.headers}")
        response = self.client.post(url, data, format='json')
        print(f"Response headers: {response.headers}")
        print(f"Superuser credentials: {self.existing_superuser.username}:{self.existing_superuser.password}")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        users = Users.objects.get(id= data['id'])
        self.assertEqual(users.submitted_by, "student1")
        
        

class StudentViewTestCase(TestCase):
    """
    Test case for the StudentView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_create_student: Test creating a student via API.
    """
    def setUp(self):
        """
        Set up the test case.

        - Initializes an API client for making requests.
        - Retrieves or creates a superuser for authentication purposes.
        """
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
        """
        Test creating a student via the API.

        - Creates an Attendence_log object for testing.
        - Defines the URL for creating students.
        - Defines the data for creating a student.
        - Authenticates with the API using superuser credentials.
        - Sends a POST request to create a student.
        - Prints request and response details for debugging.
        - Asserts that the status code is HTTP 201 Created.
        - Retrieves the created student from the database.
        - Asserts that the student attributes match the provided data.
        """
        attendence_log = Attendence_log.objects.create(id=1, Student_id=1, course_id=1, present='Yes', submitted_by='student1')
        

        url ='http://127.0.0.1:8000/api/student_create/'

        data = {
            "id":1,
            "full_name":"Prashant Baghel",
            "department_id":1,
            "classs":"2nd",
            "submitted_by":"student1"
        }
        
        
        client=self.client
        client.login(username="admin", password="123")
        print(f"Request headers: {self.client.headers}")
        response = self.client.post(url, data, format='json')
        print(f"Response headers: {response.headers}")
        print(f"Superuser credentials: {self.existing_superuser.username}:{self.existing_superuser.password}")
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        student = Student.objects.get(id= data['id'])
        self.assertEqual(student.full_name, "Prashant Baghel")
        self.assertEqual(student.department_id, 1)
        self.assertEqual(student.submitted_by, "student1")
        
        


class AttendenceListViewTestCase(TestCase):
    """
    Test case for the AttendenceListView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_list_attendence_logs: Test listing attendence logs via the API.
        - test_empty_attendence_logs: Test listing attendence logs when there are none.
    """
    def setUp(self):
        """
        Set up the test case.

        - Initializes an API client for making requests.
        - Retrieves or creates a superuser for authentication purposes.
        - Creates some Attendence_log instances for testing.
        """
        self.client = APIClient()
        self.existing_superuser = User.objects.get(username='admin')
        # Create some Attendence_log instances for testing
        Attendence_log.objects.create(Student_id=1, course_id=1, present='Yes', submitted_by='student1')
        Attendence_log.objects.create(Student_id=2, course_id=2, present='No', submitted_by='student2')

    def test_list_attendence_logs(self):
        """
        Test listing attendence logs via the API.

        - Defines the URL for listing attendence logs.
        - Authenticates with the API using superuser credentials.
        - Sends a GET request to list attendence logs.
        - Asserts that the status code is HTTP 200 OK.
        - Checks if the response contains the expected number of items.
        """

        url = 'http://127.0.0.1:8000/api/attendence_list/'  #  URL
        
        client = APIClient()
        response = client.get(url)
        client=self.client
        client.login(username="admin", password="123")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the expected number of items
        data = response.json()
        self.assertEqual(len(data), 2)  

        

    def test_empty_attendence_logs(self):
        """
        Test case when there are no Attendence_log instances.

        - Clears existing Attendence_log instances.
        - Defines the URL for listing attendence logs.
        - Sends a GET request to list attendence logs.
        - Asserts that the status code is HTTP 404 NOT FOUND.
        """

        Attendence_log.objects.all().delete()

        url = 'http://127.0.0.1:8000/api/attendence_list/'  # Replace with your actual URL

        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class AttendenceLogUpdateViewTestCase(TestCase):
    """
    Test case for the AttendenceLogUpdateView API.

    Methods:
        - setUp: Prepare necessary resources and configurations for the tests.
        - test_update_attendence_log: Test updating an attendence log via API.
    """
    def setUp(self):
        """
        Set up the test case.

        - Creates an Attendence_log instance for testing.
        """
        
        self.attendence_log = Attendence_log.objects.create(id=1,Student_id=1, course_id=1, present='Yes', submitted_by='student1')

    def test_update_attendence_log(self):
        """
        Test updating an attendence log via the API.

        - Ensures the URL includes the correct id.
        - Defines data for updating the Attendence_log.
        - Authenticates with the API using superuser credentials.
        - Prints original data before the update for debugging.
        - Sends a PATCH request to update the Attendence_log.
        - Prints the response content and status code for debugging.
        - Checks if the Attendence_log is updated in the database.
        - Prints serializer errors for debugging.
        - Asserts that the status code is HTTP 200 OK.
        """
        # Ensure the URL includes the correct id
        url = f'http://127.0.0.1:8000/api/attendnce_log_update/{self.attendence_log.id}'  #url to check

        # Data for updating the Attendence_log
        updated_data = {
            'present': 'No',
            'submitted_by': 'student2',
        }

        client = APIClient()
        #authentication logic
        client.login(username="admin", password="123")
      

        # Print the original data before the update
        print(f"Original Attendence_log present: {self.attendence_log.present}")
        print(f"Original Attendence_log submitted_by: {self.attendence_log.submitted_by}")

        response = client.patch(url, updated_data, format='json')  # Using 'patch' for partial updates

        # Print the response content for debugging
        print(response.content)

        # Print the response status code for debugging
        print(f"Response Status Code: {response.status_code}")

        # Check if the Attendence_log is updated in the database
        if response.status_code == status.HTTP_200_OK:
            updated_attendence_log = Attendence_log.objects.get(id=self.attendence_log.id)
            print(f"Updated Attendence_log present: {updated_attendence_log.present}")
            print(f"Updated Attendence_log submitted_by: {updated_attendence_log.submitted_by}")

        # Print serializer errors for debugging
        print("Serializer Errors:")
        print(response.data.get("errors"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)