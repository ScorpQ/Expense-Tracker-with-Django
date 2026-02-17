from rest_framework import serializers
from .model import Category, Expense
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'is_active']

class UserSerializer(serializers.ModelSerializer):
    expenses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Expense.objects.all()
    )
    class Meta:
        model = User
        fields = ["id", "username", "categories"]        


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'amount', 'priority', 'category', 'created_at', 'updated_at']