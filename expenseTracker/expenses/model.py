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

    # Expense eklerken dropdown'da category object yerine category name gözükmesi için __str__ methodunu ekliyoruz.
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        

class Expense(models.Model):
    HIGH = 'HG'
    MEDIUM = 'MD'
    LOW = 'LW'
    PRIORITY = {
        HIGH: "High",
        MEDIUM: "Medium",
        LOW: "Low",
    }
    
    description = models.TextField (
        null=True, 
        db_column='description', 
        db_comment= 'Expense description'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    priority = models.CharField(max_length=15, choices=PRIORITY, default=MEDIUM)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    '''owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)'''

    def save(self, *args, **kwargs):
        if not self.category:
            self.category = "Other"
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'expense'    
    
        '''
    def ___str___(self):
        return self.amount'''


