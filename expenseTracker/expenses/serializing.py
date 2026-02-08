from django.core import serializers
from .model import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'is_active']

'''
data = serializers.serialize("json", Category.objects.all())
'''