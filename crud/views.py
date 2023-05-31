from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes 
from crud.models import *
from crud.serializers import *
from rest_framework.response import Response 
from djtest.permissions import ISACTIVE,ISSTAFF,ISDIRECTOR


@api_view(['GET']) 
@permission_classes([IsAuthenticated,ISACTIVE,ISSTAFF ])
def department(request): 
    print(request)
    # if not request.user.is_director:
    #     return Response({'message': 'Access denide'}, status=403) 
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data) 



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_course(equest):
    course = Course.objects.all()
    serializer = CourseSerialiser(course, many = True)
    return Response(serializer.data)