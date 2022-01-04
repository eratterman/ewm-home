from django.contrib import admin
from finances.models import BankEntry, FinanceType, Categories, Searches


admin.site.register(BankEntry)
admin.site.register(FinanceType)
admin.site.register(Categories)
admin.site.register(Searches)
