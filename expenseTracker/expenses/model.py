from django.db import models

class Category(models.Model):
    name = models.CharField (
        max_length=30, 
        unique=True, 
        db_column='name', 
        db_comment='Category name'
    )
    description = models.TextField (
        null=True, 
        db_column='description', 
        db_comment= 'Category description'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
    '''
    def ___str___(self):
        return self.name'''


class Expense(models.Model):
    description = models.TextField (
        null=True, 
        db_column='description', 
        db_comment= 'Expense description'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'expense'    
    
        '''
    def ___str___(self):
        return self.amount'''


