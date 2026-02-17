"""
URL configuration for expenses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import CategoryList, CategoryDetail, ExpenseDetail, UserList, UserDetail, ExpenseList, some_streaming_csv_view

urlpatterns = [
    path('', CategoryList.as_view(), name='category-list'),
    path('<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path("expenses/export/", some_streaming_csv_view),
]
