from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# import basic authenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser, IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
  
#   # below authentication for locally for this f() 
    
    # authentication_classes = [SessionAuthentication]

#     # IsAuthenticated means before any crud operation user should be login otherwise can not perform any crud operation
    # permission_classes = [IsAuthenticated]
    
#   # IsAuthenticated means user login hai but phir bhi koi bhi operation perform nahi kar sakta
    # parser_classes=[IsAdminUser]


    
    # parser_classes=[IsAuthenticatedOrReadOnly]


#  admin  allow karta hai ki konsa user kon kon sa operation perform kar sakta hai 
    # parser_classes=[DjangoModelPermissions]
    
    
    
    

#  similar to DjangoModelPermissionsbut also allows unauthenticaed users to have read-only access to the API.
    # parser_classes=[DjangoModelPermissionsOrAnonReadOnly]