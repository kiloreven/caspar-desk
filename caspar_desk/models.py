from django.db import models

class Player(models.Model):
    template = models.ForeignKey(Template)

class Template(models.Model):
    name = models.CharField(max_length=128)

class Table(models.Model):
    name = models.CharField(max_length=128)
    headers = 

class TableAssignment(models.Model):
    

class TableHeader(models.Model)

class TableRow(models.Model)

class TableCell
