from django.contrib import admin
from .models import Account, Deposit, Withdrawl


admin.site.register(Account)
admin.site.register(Deposit)
admin.site.register(Withdrawl)