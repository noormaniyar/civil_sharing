from django.db import models


class Cloths(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Inward(models.Model):
    cloths = models.ForeignKey(Cloths, on_delete=models.CASCADE)
    size = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} Inward of {}".format(self.size, self.cloths)



class Outward(models.Model):
    cloths = models.ForeignKey(Cloths, on_delete=models.CASCADE)
    size = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} Outward of {}".format(self.size, self.cloths)