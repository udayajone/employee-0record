from django.contrib import admin
from empapp.models import employee
class empadmin(admin.ModelAdmin):
    emp_details=["empno","ename","salary","designation"]

admin.site.register(employee,empadmin)



# Register your models here.
