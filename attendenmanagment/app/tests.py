from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Attendence_log,Courses, Departments, Users, Student
from django.contrib.auth.models import User


class AttendenceLogViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_attendence_log(self):
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
    def setUp(self):
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
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
    def setUp(self):
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
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
    def setUp(self):
        self.client = APIClient()
        # Retrieve or create a superuser
        self.existing_superuser = User.objects.get(username='admin')
        
    def test_create_course(self):
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
    def setUp(self):
        self.client = APIClient()
        self.existing_superuser = User.objects.get(username='admin')
        # Create some Attendence_log instances for testing
        Attendence_log.objects.create(Student_id=1, course_id=1, present='Yes', submitted_by='student1')
        Attendence_log.objects.create(Student_id=2, course_id=2, present='No', submitted_by='student2')

    def test_list_attendence_logs(self):

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
        # Test case when there are no Attendence_log instances

        # Clear existing Attendence_log instances
        Attendence_log.objects.all().delete()

        url = 'http://127.0.0.1:8000/api/attendence_list/'  # Replace with your actual URL

        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class AttendenceLogUpdateViewTestCase(TestCase):
    def setUp(self):
        # Create an Attendence_log instance for testing
        self.attendence_log = Attendence_log.objects.create(id=1,Student_id=1, course_id=1, present='Yes', submitted_by='student1')

    def test_update_attendence_log(self):
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