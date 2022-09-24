from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
