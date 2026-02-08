from django.views.generic import ListView
from .model import Category

class CategoryListView(ListView):
    model = Category
