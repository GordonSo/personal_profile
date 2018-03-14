from django.db import models

# Create your models here.


class Company(models.Model):

    stock_symbol = models.CharField(verbose_name="symbol", max_length=50)


class StockRecord(models.Model):

    record_date = models.DateTimeField(verbose_name="record_date")
    symbol = models.ForeignKey(Company, on_delete=models.CASCADE)
    day_open = models.DecimalField(verbose_name="open", max_digits=10, decimal_places=10)
    day_close = models.DecimalField(verbose_name="close", max_digits=10, decimal_places=10)
    day_high = models.DecimalField(verbose_name="high", max_digits=10, decimal_places=10)
    day_low = models.DecimalField(verbose_name="low", max_digits=10, decimal_places=10)

