from django.conf.urls import url
from . import views


app_name = 'portal'

urlpatterns = [
    url(r'^accounts/$', views.AccountListView.as_view(), name='account_list'),
    url(r'^create_account/$', views.AccountCreateView.as_view(), name='create_account'),
    url(r'^update_account/(?P<id>[0-9]+)/$', views.AccountUpdateView.as_view(), name='update_account'),
    url(r'^update_deposit/(?P<id>[0-9]+)/$', views.DepositUpdateView.as_view(), name='update_deposit')


]
