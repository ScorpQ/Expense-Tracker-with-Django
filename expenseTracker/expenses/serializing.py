from rest_framework import serializers
from .model import Category, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'is_active']


class ExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(allow_blank=True, required=False)
    priority = serializers.ChoiceField(choices=Expense.PRIORITY, default=Expense.MEDIUM)
    date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        print(self, flush=True)              # ExpenseSerializer instance
        print(validated_data, flush=True)
        return Expense.objects.create(**validated_data)   