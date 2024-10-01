from rest_framework import serializers
from .models import Student


# tis is Model serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']

# above ModelSerializer have inbuild all fearture like create update etc.