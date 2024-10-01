from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# import basic authenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated  

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
  
#   # below authentication for locally for this f() 
    
#     # this line you have to write always for using authentication
#     authentication_classes = [BasicAuthentication]

#     # IsAuthenticated means only admin user opeation perform karenga and No one can perform operation on api 
#     permission_classes = [IsAuthenticated]

