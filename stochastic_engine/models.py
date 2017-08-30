from django.db import models

# Create your models here.


class Company(models.Model):

    company_symbol = models.CharField(verbose_name="symbol")


class StockRecord(models.Model):

    record_date = models.DateTimeField(verbose_name="record_date")
    symbol = models.ForeignKey(Company.company_symbol, on_delete=models.CASCADE)
    day_open = models.DecimalField(verbose_name="open")
    day_close = models.DecimalField(verbose_name="close")
    day_high = models.DecimalField(verbose_name="high")
    day_low = models.DecimalField(verbose_name="low")

