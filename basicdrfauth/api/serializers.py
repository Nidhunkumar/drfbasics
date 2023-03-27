from .models import Category,Manufacturer,Robot
from rest_framework import serializers

class Category_serializer(serializers.HyperlinkedModelSerializer):
    robots=serializers.HyperlinkedRelatedField(many=True,
      read_only=True,
      view_name='Category-detail')
    class Meta:
        model=Category
        fields='__all__'

