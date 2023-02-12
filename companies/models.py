from django.db import models
# from companies.default_imports import *
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Exchanges(TimeStampedModel):
    name = models.CharField(max_length=8, unique=True)

class Sectors(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True)

class Industries(TimeStampedModel):
    related_sector = models.ForeignKey(Sectors, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=64, unique=True)

class Countries(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True)

class States(TimeStampedModel):
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=32)

class Cities(TimeStampedModel):
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING, null=True)
    state = models.ForeignKey(States, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=32, unique=True)


class Companies(TimeStampedModel):
    exchange = models.ForeignKey(Exchanges, on_delete=models.DO_NOTHING)
    symbol = models.CharField(max_length=8, unique=True)
    shortname = models.CharField(max_length=64)
    longname = models.CharField(max_length=128)
    industry = models.ForeignKey(Industries, on_delete=models.DO_NOTHING, null=True)
    current_price = models.FloatField(null=True)
    marketcap = models.BigIntegerField(null=True)
    ebitda = models.BigIntegerField(null=True)
    revenue_growth = models.FloatField(null=True)
    city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING, null=True)
    full_time_employees = models.IntegerField(null=True)
    long_business_summary = models.TextField(null=True)
    weight = models.FloatField(null=True)
