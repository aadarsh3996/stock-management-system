from django.db import models

# Create your models here.

class CompanyList(models.Model):
    company_symbol=models.CharField(max_length=10)
    company_name=models.CharField(max_length=40)
    company_last_sale=models.CharField(max_length=10)
    company_market_cap=models.CharField(max_length=10)
    company_ipo_year=models.CharField(max_length=5)
    company_sector=models.CharField(max_length=20)
    company_industry=models.CharField(max_length=60)
    comany_summary_quote=models.CharField(max_length=60)


class Order(models.Model):
    username = models.CharField(max_length=30)
    bs = models.CharField(max_length=4)
    sname = models.CharField(max_length=50)
    sprice = models.CharField(max_length=10)
    squantity = models.CharField(max_length=20)
    ssymbol = models.CharField(max_length=8)
    total_worth = models.CharField(max_length=25)


class Track(models.Model):
    username = models.CharField(max_length=30)
    squantity = models.CharField(max_length=10)
    ssymbol = models.CharField(max_length=8)
    sname = models.CharField(max_length=50)
