from django.utils import timezone
from django.db import models

# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "departments"
        verbose_name = 'Departments'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class SubDepartments(models.Model):
    name = models.CharField(max_length=250)
    short_dep_name = models.CharField(max_length=20, null=True)
    code = models.IntegerField(null=True)
    barcode_print_flag = models.BooleanField(default=True)
    email_flag = models.BooleanField(default=True)
    sms_flag = models.BooleanField(default=True)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)
    departments = models.ForeignKey(
        Departments, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "sub_departments"
        verbose_name = 'Sub Departments'
        verbose_name_plural = 'Sub Departments'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    flag_status = models.CharField(max_length=1)
    mobileno = models.IntegerField()
    report_mail_flag = models.CharField(max_length=1)
    report_login_id = models.CharField(max_length=100)
    report_password = models.CharField(max_length=100)
    int_code = models.CharField(max_length=100)
    last_modified_on = models.DateField()
    dob = models.DateField()
    anniversary_date = models.DateField()
    license_no = models.CharField(max_length=200)
    pro_name = models.CharField(max_length=200)
    # creationid=models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)

    class Meta:
        db_table = "Doctor"
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctor'

    def __str__(self):
        return self.doctor_name
