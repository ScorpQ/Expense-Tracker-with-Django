
from .model import Category
from rest_framework import generics, request, response, status
from .serializing import CategorySerializer
from rest_framework.views import APIView

''' Bu kısım rest api yerine templete render yapısı için kullanıldı.
class CategoryListView(ListView):
    model = Category
'''

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return response.Response(serializer.data)
    
    def post(self, request, format=None):
        categories = CategorySerializer(data=request.data)
        if categories.is_valid():
            categories.save()
            return response.Response(categories.data, status=status.HTTP_201_CREATED)
        return response.Response(categories.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise response.Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self, request, pk, format=None):
        category = self.get_category(pk)
        categorySerializer = CategorySerializer(category)
        return response.Response(categorySerializer.data)
    
    def put(self, request, pk, format=None):
        category = self.get_category(pk)
        categorySerializer = CategorySerializer(category, data=request.data)
        if categorySerializer.is_valid():
            categorySerializer.save()
            return response.Response(categorySerializer.data)
        return response.Response(categorySerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_category(pk)
        category.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)