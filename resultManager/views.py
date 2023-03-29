from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Score, Student

@api_view(['POST'])
def submit_student_data(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def view_student_results(request):
    
    results = Student.objects.all()
    serializer = StudentSerializer(results, many=True)
    return Response(serializer.data, status=200)
    
@api_view(['GET'])
def view_student_results(request,pk):
    
    results = Student.objects.filter(id=pk)
    serializer = StudentSerializer(results, many=True)
    return Response(serializer.data, status=200)