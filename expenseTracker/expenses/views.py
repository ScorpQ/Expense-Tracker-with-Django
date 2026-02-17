import csv
from django.http import HttpResponse, StreamingHttpResponse
import django_filters
from django.db.models import Sum
from rest_framework import generics
from .model import Category, Expense
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from .serializing import CategorySerializer, UserSerializer, ExpenseSerializer


## LISTING ##
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    ### http://127.0.0.1:8000/expenses/?start_date=2026-02-16
    def get_queryset(self):
        return get_filtered_expenses(self.request)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        total_amount = queryset.aggregate(total=Sum("amount"))["total"]
        response.data = {
            "total_amount": total_amount,
            "expenses": response.data
        }
        return response



## DETAILS ##
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer



## USERS ##
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


## EXPORT ##
class Echo:
    def write(self, value):
        return value


def some_streaming_csv_view(request):
    queryset = get_filtered_expenses(request).select_related("category")

    def row_generator():
        yield ["id", "description", "amount", "category", "date"]

        for expense in queryset.iterator():
            yield [
                expense.id,
                expense.description,
                expense.amount,
                expense.category.name if expense.category else "",
                expense.date,
            ]

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)

    return StreamingHttpResponse(
        (writer.writerow(row) for row in row_generator()),
        content_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="expenses.csv"'},
    )





## FILTERING FUNC ###
### http://127.0.0.1:8000/expenses/?start_date=2026-02-16
def get_filtered_expenses(request):

    # Get all results from DB
    queryset = Expense.objects.all()

    category = request.GET.get("category")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    start_date = parse_date(start_date) if start_date else None
    end_date = parse_date(end_date) if end_date else None

    if start_date:
        queryset = queryset.filter(created_at__gte=start_date)

    if end_date:
        queryset = queryset.filter(created_at__lte=end_date)

    if category:
        queryset = queryset.filter(category__id=category)

    return queryset