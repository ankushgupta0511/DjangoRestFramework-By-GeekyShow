from rest_framework import serializers
from .models import Student



# // defind validator Validation
def start_with_r(value):
    if value[0].lower() !=  'r':
        raise serializers.ValidationError('Name shoud be start with R')



#//  this is Model searializer class
class StudentSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model = Student
        fields = ['name','roll','city']

    
    
#// Field Lavel Validation
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    
    
#// Object Lavel Validation
    def validate(self, data):
        nm =data.get('name')
        ct =data.get('city')

        if nm.lower() == 'ankush' and ct.lower() != 'bhopal':
            raise serializers.ValidationError('City must be Ranchi')
        return data
    
    
