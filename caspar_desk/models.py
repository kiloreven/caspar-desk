from django.db import models

class NameList(models.Model):
    name = models.CharField(max_length=32)

class NameListItem(models.Model):
    line1 = models.CharField(max_length=64, default='')
    line2 = models.CharField(max_length=64, default='')
    list = models.ForeignKey(NameList)



