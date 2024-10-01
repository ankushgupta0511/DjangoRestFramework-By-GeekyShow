from rest_framework import serializers
from .models import Student


# // Ttis is Model serializer
class StudentSerializer(serializers.ModelSerializer):


    # // name can be read and create but can not be update  but other field can be update 
    # name = serializers.CharField(read_only=True)  

    
    class Meta:
        model = Student
        fields = ['name','roll','city']
        
        
        # // below 'read_only' apply on multyple attribue 
        # read_only_fields = ['name','roll']
        
        
        
        # // this is the other way to give argument on attributes
        extra_kwargs = {'name':{'read_only':True},'roll':{'read_only':True}}



# above ModelSerializer have inbuild all fearture like create update etc.