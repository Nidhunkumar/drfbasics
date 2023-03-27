# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Category,Manufacturer,Robot
from api.serializers import Category_serializer

class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'robot-categories': reverse(RobotCategoryList.name, request=request),
            
            })    
class RobotCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class  = Category_serializer
    name = 'robotcategory-list'

