
from rest_framework import serializers
from .models import *

# from dataclasses import field
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'



class CourseSerialiser(serializers.ModelSerializer):
    class Meta:
        models = Course
        fields = "__all__"