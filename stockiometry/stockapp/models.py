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
