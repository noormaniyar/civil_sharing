from django.db import models
from django.db.models.signals import post_save


class Material(models.Model):
    name = models.CharField(max_length=200)
    current_weight = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Inward(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()

    def __str__(self):
        return "{} Inward of {}".format(self.weight, self.material)


def add_inward_weight(sender, instance, created, *args, **kwargs):
    if created:
        inward = instance
        material = inward.material
        material.current_weight = material.current_weight + inward.weight
        material.save()

post_save.connect(add_inward_weight, sender=Inward)




class Outward(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()

    def __str__(self):
        return "{} Outward of {}".format(self.weight, self.material)


def add_outward_weight(sender, instance, created, *args, **kwargs):
    if created:
        outward = instance
        material = outward.material
        material.current_weight = material.current_weight - outward.weight
        material.save()

post_save.connect(add_outward_weight, sender=Outward)











