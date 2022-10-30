from pyexpat import model
from django.db import models
from account.models import Account
# Create your models here.
class FacultyInfo(models.Model):
    fct_id = models.AutoField(primary_key=True)
    fct_name = models.CharField(max_length=50)
    fct_entry_date = models.DateTimeField(auto_now_add=True)
    fct_lastmodify_date = models.DateTimeField(auto_now=True)
    fct_active = models.BooleanField(default=True)

class DepartmentInfo(models.Model):
    dpt_id = models.AutoField(primary_key=True)
    dpt_name = models.CharField(max_length=50)
    dpt_entry_date = models.DateTimeField(auto_now_add=True)
    dpt_lastmodify_date = models.DateTimeField(auto_now=True)
    dpt_active = models.BooleanField(default=True)
    dpt_faculty = models.ForeignKey(FacultyInfo, on_delete=models.CASCADE)

class SubjectInfo(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=50)
    sub_unit = models.SmallIntegerField()
    sub_seat = models.SmallIntegerField()
    sub_schedule = models.CharField(max_length=50) # store cron expression
    sub_entry_date = models.DateTimeField(auto_now_add=True)
    sub_lastmodify_date = models.DateTimeField(auto_now=True)
    sub_active = models.BooleanField(default=True)
    sub_department = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE)

class EnrollInfo(models.Model):
    nrl_id = models.AutoField(primary_key=True)
    nrl_student = models.ForeignKey(Account, on_delete=models.CASCADE)
    nrl_subject = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE)
    nrl_status = models.CharField(max_length=20, default='On processing')
    nrl_entry_date = models.DateTimeField(auto_now_add=True)
    nrl_lastmodify_date = models.DateTimeField(auto_now=True)
    nrl_active = models.BooleanField(default=True)