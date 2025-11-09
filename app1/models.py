from django.db import models

# Create your models here.
class contactusdata(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=150,null=False)
    phone=models.CharField(max_length=30,null=False)
    subject=models.CharField(max_length=200,null=False)
    message=models.TextField(null=False)

#model for submission of appointment data
class appointdata(models.Model):
    apname=models.CharField(max_length=100,null=False)
    apemail=models.CharField(max_length=200,null=False)
    apphone=models.CharField(max_length=50,null=False)
    apdepart=models.CharField(max_length=100,null=False)
    apdate=models.CharField(max_length=100,null=False)
    apdoctor=models.CharField(max_length=100,null=False)
    apmessage=models.TextField(null=False)

#model for signup of data
class registerdataa(models.Model):
    regfname=models.CharField(max_length=100,null=False)
    reglname=models.CharField(max_length=100,null=False)
    regemail=models.CharField(max_length=100,null=False)
    regphone=models.CharField(max_length=50,null=False)
    regpassword=models.CharField(max_length=150,null=False)
