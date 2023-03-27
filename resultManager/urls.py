from django.urls import path
from .views import submit_student_data

urlpatterns = [
    path('students/', submit_student_data, name='submit_student_data'),
]