from .models import Attendence_log, Courses, Users,Departments, Student

from rest_framework import serializers


class Attendence_serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence_log
        fields = '__all__'
     
    
    
    



class Courses_serializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
    
         
    

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class Departments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class Students_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

