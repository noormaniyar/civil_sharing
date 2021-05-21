from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Account, Deposit, Withdrawl
from django.urls.base import reverse_lazy


class AccountListView(ListView):
    model = Account
    template_name = 'portal/account_list.html'
    context_object_name = 'all_accounts'
    ordering = '-balance'


class AccountCreateView(CreateView):
    model = Account
    template_name = 'portal/create_account.html'
    fields = ['full_name', 'address', 'pan_number', 'mobile_number']
    success_url = reverse_lazy('portal:account_list')



class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'portal/update_account.html'
    fields = ['full_name', 'address', 'pan_number', 'mobile_number']
    success_url = reverse_lazy('portal:account_list')
    pk_url_kwarg = 'id'

class DepositUpdateView(UpdateView):
    model = Deposit
    template_name = 'portal/update_deposit.html'
    fields = ['account', 'amount', 'deposited_on', 'deposited_by']
    success_url = reverse_lazy('portal:account_list')
    pk_url_kwarg = 'id'