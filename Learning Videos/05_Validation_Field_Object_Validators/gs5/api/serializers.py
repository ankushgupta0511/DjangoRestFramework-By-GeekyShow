from rest_framework import serializers
from .models import Student


# // defind validator Validation
def start_with_r(value):
    if value[0].lower() !=  'r':
        raise serializers.ValidationError('Name shoud be start with R')



# // this is Regular searializer class
class StudentSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length=100)


# // validator Validation

# name should be start with r otherwise not create student object
    name = serializers.CharField(max_length=100,validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
   
   
   
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    
    def update(self, instance,validated_data):
        print(instance.name)    #  'ankush' old value
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)    # 'ankush gupta' new updated value
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        
        instance.save()
        return instance
    
    
    
# Field Lavel Validation
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    
    
# Object Lavel Validation
    def validate(self, data):
        nm =data.get('name')
        ct =data.get('city')

        if nm.lower() == 'ankush' and ct.lower() != 'bhopal':
            raise serializers.ValidationError('City must be Ranchi')
        return data