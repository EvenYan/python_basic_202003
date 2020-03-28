from django.db import models

# Create your models here.

class PeopleInfo(models.Model):
    name = models.CharField(max_length=40)
    passwd = models.CharField(max_length=40, default="root")
    phone_num = models.CharField(max_length=11)

    def __str__(self):
        return self.name