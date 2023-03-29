from django.urls import path
from .views import submit_student_data, view_student_results

urlpatterns = [
    path('students/', submit_student_data, name='submit_student_data'),
    path('results/', view_student_results, name='view_student_results'),
    path('results/<pk>', view_student_results, name='view_student_results'),

]