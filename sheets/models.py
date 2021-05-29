from django.db import models

# Create your models here.


class Sheet(models.Model):
    rows = models.IntegerField()
    columns = models.IntegerField()
    def __str__(self):
        return "Sheet with {} rows and {} columns".format(self.rows,self.columns)


class SheetData(models.Model):
    data = models.CharField(max_length=10000)
    def __str__(self):
        return "data Added {}".format(self.data)