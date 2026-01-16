from django.db import models

class Cat(models.Model):
    class Meta:
        db_table = "cats"

    name = models.CharField(max_length=20, null=False)
    years_of_experience = models.PositiveSmallIntegerField(null=False)
    breed = models.CharField(null=False)
    salary = models.FloatField(null=False)


class Mission(models.Model):
    class Meta:
        db_table = "missions"

    cat = models.ForeignKey("Cat", unique=True, on_delete=models.CASCADE, null=False)
    is_completed = models.BooleanField(default=False, null=False)


class Target(models.Model):
    class Meta:
        db_table = "targets"
    
    mission = models.ForeignKey("Mission", related_name="targets", on_delete=models.CASCADE, null=False)
    name = models.CharField(null=False, max_length=20)
    country = models.CharField(max_length=25, null=False)
    notes = models.TextField(null=False, blank=True)
    is_completed = models.BooleanField(default=False, null=False)
