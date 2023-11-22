from django.urls import path
from .views import  Attendence_log_view, cousre_vieW, users_view,department_view, Student_view,attendence_list_view, course_list_view,user_list_view, department_list_view, student_list_view,Attendence_log_Update_view,course__Update_view, users__Update_view, department__Update_view, Student__Update_view

urlpatterns = [
    #path('api/user_create/', UserCreateView.as_view(), name='user-create'),
    path('api/attendence_log_create/', Attendence_log_view.as_view(), name='attendnce_log_create'),
    path('api/course_create/', cousre_vieW.as_view(), name='course_create'),
    path('api/user_createe/', users_view.as_view(), name='user_create'),
    path('api/department_create/', department_view.as_view(), name='department_create'),
    path('api/student_create/', Student_view.as_view(), name='student_create'),
    path('api/attendence_list/', attendence_list_view.as_view(), name='attendence_list'),
    path('api/course_list/', course_list_view.as_view(), name='course_list'),
    path('api/user_list/', user_list_view.as_view(), name='user_list'),
    path('api/department_list/', department_list_view.as_view(), name='dept_list'),
    path('api/student_list/', student_list_view.as_view(), name='student_list'),
    path('api/attendnce_log_update/<int:id>', Attendence_log_Update_view.as_view(), name='attendnce_log_update'),
    path('api/course_update/<int:id>', course__Update_view.as_view(), name='course_update'),
    path('api/user_update/<int:id>', users__Update_view.as_view(), name='user_update'),
    path('api/dept_update/<int:id>', department__Update_view.as_view(), name='dept_update'),
    path('api/student_update/<int:id>', Student__Update_view.as_view(), name='Student_update'),

    

    






    


    #path('members/', views.members, name='members'),
]