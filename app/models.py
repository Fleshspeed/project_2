from django.db import models


# class Book(models.Model):
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()

#     def __str__(self):
#         return self.author



class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    roles = models.CharField(max_length=255)
    

    def __str__(self):
        return self.roles