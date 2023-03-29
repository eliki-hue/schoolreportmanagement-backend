from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import generics, status
from rest_framework.views import APIView 
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
def view_all_students_results(request):
    
    results = Student.objects.all()
    serializer = StudentSerializer(results, many=True)
    return Response(serializer.data, status=200)
    
@api_view(['GET'])
def view_student_results(request,pk):
    
    results = Student.objects.filter(id=pk)
    serializer = StudentSerializer(results, many=True)
    return Response(serializer.data, status=200)

class result_Update(APIView):
    def put(self,request, pk):
        item = Student.objects.get(pk=pk)
        data = StudentSerializer(instance=item, data=request.data)
    
        if data.is_valid():
            item.name =request.data['name']
            item.scores =request.data['scores']
            item.email =request.data['email']
            item.save()
            return Response(data.data)
        else:
            return Response("VALUES SUPPLIED NOT VALID", status=status.HTTP_404_NOT_FOUND)


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer