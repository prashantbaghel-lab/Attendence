from django.contrib import admin
from .models import Attendence_log, Courses, Users, Departments, Student

# Register your models here.
admin.site.register(Attendence_log)
admin.site.register(Courses)
admin.site.register(Users)
admin.site.register(Departments)
admin.site.register(Student)



