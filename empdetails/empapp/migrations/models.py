from django.db import models

class employee(models.Model):

     PROGRAMMER ="PROGRAMMER"
     MANAGER = "MANAGER"
     DESIGNATION_CHOICE =((PROGRAMMER,"PROGRAMMER"),(MANAGER,"MANAGER"))
     empno=models.IntegerField(primary_key= True)
     ename=models.CharField(max_length=10)
     salary=models.FloatField()
     designation=models.CharField(max_length=20,choices= DESIGNATION_CHOICE)


