from django.db import models


# Create your models here.
class Customer(models.Model):
    phone1 = models.CharField(null=True,blank=False, unique = False, max_length=12)
    phone2 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    kanjiname=models.CharField(max_length=50, null=True, default=None)
    kanjilastname=models.CharField(max_length=50, null=True, default=None)
    kananame=models.CharField(max_length=50, null=True, default=None)
    kanalastname=models.CharField(max_length=50, null=True, default=None)
    dob = models.DateField(null=True, default=None)
    gender=models.CharField(max_length=50, null=True, default=None)
    add1=models.CharField(null=True,blank=False, unique = False, max_length=50)
    add2=models.CharField(null=True,blank=False, unique = False, max_length=50)
    add3=models.CharField(max_length=100, default=None, null=True)
    email=models.EmailField(null=True,blank=False, unique = True)
    cell1 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    cell2 = models.CharField(null=True,blank=False, unique = True, max_length=12)

    # phone1 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    # phone2 = models.CharField(null=True,blank=False, unique = True, max_length=12)
    # country_code = models.CharField(null=True,blank=False, unique = True, max_length=4)
    # kanjiname=models.CharField(max_length=10, null=True, default=None)
    # kanjilastname=models.CharField(max_length=10, null=True, default=None)
    # kananame=models.CharField(max_length=10, null=True, default=None)
    # kanalastname=models.CharField(max_length=10, null=True, default=None)
    # date_of_birth = models.DateField(null=True, default=None)
    # gender=models.CharField(max_length=50, null=True, default=None)
    # Zipcode=models.IntegerField(null=True,blank=False, unique = False)
    # add1=models.CharField(null=True,blank=False, unique = False, max_length=50)
    # add2=models.IntegerField(null=True,blank=False, unique = True)
    # add3=models.CharField(max_length=100, default=None, null=True)
    # email=models.EmailField(null=True,blank=False, unique = False)