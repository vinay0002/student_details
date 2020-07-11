from django.db import models


class Studentmodel(models.Model):
    Student_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=150)
    Gender = models.CharField(max_length=150)
    Age = models.CharField(max_length=150)
    Class = models.CharField(max_length=150)
    Address = models.TextField()

    def __str__(self):
        return self.Name

class Marksmodel(models.Model):
    Mathes = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    English = models.IntegerField()
    social_studies= models.IntegerField()
    Student_id = models.ForeignKey('Studentmodel', related_name='marks', on_delete=models.CASCADE)



