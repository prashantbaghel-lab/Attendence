from django.db import models

# Create your models here.
class Attendence_log(models.Model):
    id=models.IntegerField(primary_key=True)
    Student_id= models.IntegerField()
    course_id=models.IntegerField()
    present=models.CharField(max_length=3)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __int__(self):
        return self.id
    
#creation of model for courses
class Courses(models.Model):
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE,primary_key=True )
    course_name=models.CharField(max_length=100)
    department_id=models.IntegerField()

    semester=models.CharField(max_length=5)
    classs=models.CharField(max_length=5)
    lecture_hours=models.CharField(max_length=5)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.course_id
    
#creation model for Departments 
class Departments(models.Model):
    id=models.OneToOneField(Courses, on_delete=models.CASCADE, primary_key=True)
 
    department_name=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __int__(self):
        return self.dept_id


# creation model for Users 
class Users(models.Model):
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE, primary_key=True)
    type_user=models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __int__(self):
        return self.user_id

# creation model for Student 

class Student(models.Model):
    id=models.OneToOneField(Attendence_log, on_delete=models.CASCADE, primary_key=True)
    full_name=models.CharField(max_length=100)
    department_id= models.IntegerField(default=1)
    classs=models.CharField(max_length=100)
    submitted_by=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __int__(self):
        return self.student_id


