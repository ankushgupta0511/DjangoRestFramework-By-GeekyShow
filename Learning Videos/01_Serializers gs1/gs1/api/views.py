from django.shortcuts import render

# Create your views here.

# model object - single Student Data
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse



# when single instance given
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)    # complex data type   or model instance
    serializer = StudentSerializer(stu)   # convert python data


    # below both line can replace by JsonResponse()
    # json_data = JSONRenderer().render(serializer.data)    # python data convert into json
    # return HttpResponse(json_data,content_type = 'application/json')

    return JsonResponse(serializer.data,safe=True)   # it return single json isliye 'safe=True'



# when queryset :- All Student Data given
def student_list(request):
    stu = Student.objects.all()    # complex data type   or model instance
    print(stu)
    serializer = StudentSerializer(stu, many=True)   # convert python data
    
    # below both line can replace by JsonResponse()
    # json_data = JSONRenderer().render(serializer.data)    # python data convert into json
    # return HttpResponse(json_data,content_type = 'application/json')     

    
    return JsonResponse(serializer.data,safe=False)   # it return list of json   isliye 'safe=True'
    
