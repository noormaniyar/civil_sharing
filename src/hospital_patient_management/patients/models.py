from django.db import models





class Bed(models.Model):
    bed_name = models.CharField(max_length=32, unique=True)
    extra_info = models.TextField()

    def __str__(self):
        return str(self.bed_name)



class Patient(models.Model):
    full_name = models.CharField(max_length=200)
    bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, blank=True, null=True)
    treatment = models.CharField(max_length=500)
    hospitalized_on = models.DateTimeField(auto_now_add=True)
    is_discharge = models.BooleanField(default=False)
    discharged_on = models.DateTimeField(blank=True, null=True)
    bill = models.PositiveIntegerField(blank=True, null=True)
    extra_info = models.TextField()


    def __str__(self):
        return str(self.full_name)
