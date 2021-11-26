import datetime
from django.db import models


class BankData(models.Model):
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

    def __repr__(self):
        return f'<bank data object: {self.display}>'


class Categories(models.Model):
    category = models.CharField(max_length=200)

    def __repr__(self):
        return f'<category object: {self.category}>'