from django.db import models




class Account(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    pan_number = models.CharField(max_length=15)
    account_number = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=10)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.full_name



class Deposit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    deposited_on = models.DateTimeField()
    deposited_by = models.CharField(max_length=100)

    def __str__(self):
        return self.deposited_by



class Withdrawl(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    withdrawl_on = models.DateTimeField()
    withdrawl_by = models.CharField(max_length=100)

    def __str__(self):
        return self.withdrawl_by
