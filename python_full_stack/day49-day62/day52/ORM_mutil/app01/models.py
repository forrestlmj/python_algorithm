from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    objects = models.Manager()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Publish(models.Model):

    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    objects = models.Manager()



class Author(models.Model):
    name = models.CharField(max_length=32)
    objects = models.Manager()
