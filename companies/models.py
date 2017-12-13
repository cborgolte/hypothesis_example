from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Shop(models.Model):
    name = models.CharField(max_length=36)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.company} - {self.name} ({self.id})'
