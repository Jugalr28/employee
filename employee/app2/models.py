from django.db import models

class Student(models.Model):

    ename=models.CharField(max_length=100)
    age=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    cover=models.ImageField(upload_to='images')

    def __str__(self):
        return self.ename
