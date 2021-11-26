import datetime
from django.db import models


class BankEntry(models.Model):
    """
    holds each entry from the bank
    """
    display = models.CharField(max_length=100, db_index=True)
    account = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        db_index=True
    )
    check_num = models.IntegerField(db_index=True)
    has_cleared = models.BooleanField(default=False)
    create_date = models.DateTimeField(
        default=datetime.datetime.now,
        db_index=True
    )
    bank_date = models.DateField(db_index=True)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Bank Entry'

    def __repr__(self):
        return f'<bank data object: {self.display}>'


class FinanceType(models.Model):
    """
    two finance types: Income or Expense
    """
    finance_type = models.CharField(max_length=25, db_index=True)

    class Meta:
        verbose_name = 'Finance Type'

    def __repr__(self):
        return f'<finance type object: {self.finance_type}>'


class Categories(models.Model):
    """
    Finance category ex:
        auto, home, cleaning, pets
    """
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Categories'

    def __repr__(self):
        return f'<category object: {self.category}>'


class Searches(models.Model):
    search = models.CharField(max_length=200, db_index=True)
    display = models.CharField(max_length=500, db_index=True)
    account = models.CharField(max_length=50, db_index=True)
    finance_type = models.ForeignKey(
        FinanceType,
        on_delete=models.PROTECT,
        related_name='fin_type'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT,
        related_name='fin_category'
    )

    class Meta:
        verbose_name = 'Searches'

    def __repr__(self):
        return f'<search object: {self.display}>'
