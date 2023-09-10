from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=512)
    start_data = models.DateField(blank=True, null=True)
    is_activate = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    KOLLAGE = 'kollage'
    UNVERSITY = 'unversity'
    MAGISTER = 'magister'
    LVLS = (
        (KOLLAGE, 'kollage'),
        (UNVERSITY, 'unversity'),
        (MAGISTER, 'magister'),
    )
    frist_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    degree = models.CharField(max_length=120, choices=LVLS)

    def __str__(self):
        return f'{self.frist_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=120)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f'{self.name}'
