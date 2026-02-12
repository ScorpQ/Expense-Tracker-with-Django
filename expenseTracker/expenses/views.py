from .model import Expense
from .model import Category
from rest_framework import generics
from .serializing import ExpenseSerializer
from .serializing import CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer