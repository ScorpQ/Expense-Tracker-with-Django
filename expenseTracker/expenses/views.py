from django.views.generic import ListView
from .model import Category

from rest_framework import generics
from .serializing import CategorySerializer


class CategoryListView(ListView):
    model = Category

class CategoryListButVideo(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer