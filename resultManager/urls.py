from django.urls import path
from . import views
urlpatterns = [
    path('submit_students_results/', views.submit_student_data, name='submit_student_data'),
    path('get_all_results/', views.view_all_students_results, name='view_student_results'),
    path('get_single_results/<pk>', views.view_student_results, name='view_student_results'),
    path('update_students/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),

]