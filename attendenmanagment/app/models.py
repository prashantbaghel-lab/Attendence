from django.db import models

# Create your models here.
class Attendence_log(models.Model):
    """
    Model representing attendance logs.

    Fields:
        - id: Auto-incremented primary key.
        - student_id: ID of the student.
        - course_id: ID of the course.
        - present: Indicates attendance status.
        - submitted_by: User submitting the attendance log.
        - updated_at: Date and time of log creation.

    Methods:
        - __str__: Human-readable representation of the attendance log.
    """
    id=models.IntegerField(primary_key=True)
    Student_id= models.IntegerField()
    course_id=models.IntegerField()
    present=models.CharField(max_length=3)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Attendance Log {self.id}"
    
#creation of model for courses
class Courses(models.Model):
    """
    Model representing courses.

    Fields:
        - id: One-to-one relationship with Attendence_log for a unique course.
        - course_name: Name of the course.
        - department_id: ID of the department offering the course.
        - semester: Semester in which the course is offered.
        - classs: Class identifier for the course.
        - lecture_hours: Number of lecture hours for the course.
        - submitted_by: User submitting the course information.
        - updated_at: Date and time of course creation.

    Methods:
        - __str__: Human-readable representation of the course.
    """
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE,primary_key=True )
    course_name=models.CharField(max_length=100)
    department_id=models.IntegerField()

    semester=models.CharField(max_length=5)
    classs=models.CharField(max_length=5)
    lecture_hours=models.CharField(max_length=5)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Course: {self.course_name}"
    
#creation model for Departments 
class Departments(models.Model):
    """
    Model representing departments.

    Fields:
        - id: One-to-one relationship with Courses for a unique department.
        - department_name: Name of the department.
        - submitted_by: User submitting the department information.
        - updated_at: Date and time of department creation.

    Methods:
        - __str__: Human-readable representation of the department.
    """
    id=models.OneToOneField(Courses, on_delete=models.CASCADE, primary_key=True)
 
    department_name=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Department: {self.department_name}"


# creation model for Users 
class Users(models.Model):
    """
    Model representing users.

    Fields:
        - id: One-to-one relationship with Attendence_log for a unique user.
        - type_user: Type of user (e.g., admin, student).
        - full_name: Full name of the user.
        - username: Username of the user.
        - email: Email address of the user.
        - password: Password of the user.
        - submitted_by: User submitting the user information.
        - updated_at: Date and time of user creation.

    Methods:
        - __str__: Human-readable representation of the user.
    """
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE, primary_key=True)
    type_user=models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"User: {self.username}"

# creation model for Student 

class Student(models.Model):
    """
    Model representing students.

    Fields:
        - id: One-to-one relationship with Attendence_log for a unique student.
        - full_name: Full name of the student.
        - department_id: ID of the department to which the student belongs.
        - classs: Class identifier for the student.
        - submitted_by: User submitting the student information.
        - updated_at: Date and time of student creation.

    Methods:
        - __str__: Human-readable representation of the student.
    """
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE, primary_key=True)
    full_name=models.CharField(max_length=100)
    department_id= models.IntegerField(default=1)
    classs=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Student: {self.full_name}"


