from django.db import models

class FinanceSheet(models.Model):
    STATUS_CHOICES = (
    ('expenses', 'Expenses'),
    ('income', 'Income'),
    ('savings', 'Savings'),
    )

    tdate = models.DateField("Date of Transaction")
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    statement = models.CharField('Statement', max_length=10, choices=STATUS_CHOICES, default='expenses')

    def __str__(self):
        return self.title