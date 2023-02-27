from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Student

# Create your views here.

@api_view(['POST'])
def add_student(request):
    params = request.data
    serialized_data = StudentSerializer(data = params)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'status_code':201,'message':'Student details added successfully'})
    else:
    
        return JsonResponse({'status_code':402,'message':'Form error'})
@api_view(['GET'])    
def view_student(request):
    students = Student.objects.all()
    serialised_data = StudentSerializer(students,many = True)
    return Response({'student_list':serialised_data.data})


@api_view(['DELETE'])
def delete_student(request,id):
    try:
        students = Student.objects.get(id = id )
        students.delete()

        return Response({'status_code':200,'message':'deleted successfully'})
    
    except:
        return Response({'message':'id not found'})
    
@api_view(['PUT'])
def update_student(request,id):
        student = Student.objects.get(id = id )
        serialised_data = StudentSerializer(student, data = request.data)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response({'status_code':201,'message':'Student details updated successfully'})
        else:
    
            return Response({'status_code':402,'message':'Form error'})
        








