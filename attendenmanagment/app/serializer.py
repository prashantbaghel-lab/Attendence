from .models import Attendence_log,  Users, Student, Departments, Courses

from rest_framework import serializers


#serializer for Attendence log model
class Attendence_serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence_log
        fields = '__all__'
    def Post(request):
        if request.method == "POST":

            def validate(self, data):
                
                # user = data['user']
                exit_id = data.get('id')

                # Check if the user has already created an exit with the given ID
                existing_exit = Attendence_log.objects.filter(id=exit_id).first()

                if existing_exit:
                    raise serializers.ValidationError(f"User has already created an exit with ID {exit_id}.")

                return data
     
    
    
    


#Serializer for Course Model
class Courses_serializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
    
    def Post(request):
        if request.method == "POST":

            def validate(self, data):
                # user = data['user']
                exit_id = data.get('id')

                # Check if the course has already created an exit with the given ID
                existing_exit = Attendence_log.objects.filter(id=exit_id).first()

                if existing_exit:
                    raise serializers.ValidationError(f"User has already created an exit with ID {exit_id}.")

                return data
    
         
    
#Serializer for User Model

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    def Post(request):
        if request.method == "POST":

            def validate(self, data):
            
                exit_id = data.get('id')

                # Check if the user has already created an exit with the given ID
                existing_exit = Attendence_log.objects.filter(id=exit_id).first()

                if existing_exit:
                    raise serializers.ValidationError(f"User has already created an exit with ID {exit_id}.")

                return data

#Serializer for Departments Model
class Departments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
    def Post(request):
        if request.method == "POST":

            def validate(self, data):
                # user = data['user']
                exit_id = data.get('id')

                # Check if the Departments has already created an exit with the given ID
                existing_exit = Attendence_log.objects.filter(id=exit_id).first()

                if existing_exit:
                    raise serializers.ValidationError(f"User has already created an exit with ID {exit_id}.")

                return data

#Serializer for Student Model
class Students_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def Post(request):
        if request.method == "POST":

            def validate(self, data):
                # user = data['user']
                exit_id = data.get('id')

                # Check if the Student has already created an exit with the given ID
                existing_exit = Attendence_log.objects.filter(id=exit_id).first()

                if existing_exit:
                    raise serializers.ValidationError(f"User has already created an exit with ID {exit_id}.")

                return data

