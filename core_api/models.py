from email.policy import default
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
    full_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    flag_status = models.CharField(max_length=1)
    # mobileno = models.IntegerField()
    report_mail_flag = models.CharField(max_length=1)
    report_login_id = models.CharField(max_length=100)
    report_password = models.CharField(max_length=100)
    int_code = models.CharField(max_length=100)
    # last_modified_on = models.DateField()
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
        return self.full_name


class Parameters(models.Model):
    name = models.CharField(max_length=250, null=True)
    report_name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=30)
    rate = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    method = models.CharField(max_length=30)
    suffix = models.CharField(max_length=2)
    formulae = models.CharField(max_length=100)
    dc = models.CharField(max_length=1)
    precision = models.IntegerField()
    default_status = models.CharField(max_length=1)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)
    is_required = models.BooleanField(default=True)

    class Meta:
        db_table = "parameters"
        verbose_name = 'Parameters'
        verbose_name_plural = 'Parameters'


class Sampletype(models.Model):

    STATUS_CHOICES = [
        ('A', 'Register'),
        ('B', 'Sample Collect'),
        ('C', 'Sample Accept')
    ]

    name = models.CharField(max_length=200)
    sample_type = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='A', unique=True)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "sampletype"
        verbose_name = 'Sampletype'
        verbose_name_plural = 'Sampletype'

    def __str__(self):
        return self.name


class Titles(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=200)
    display_order = models.IntegerField()
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M', unique=True)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Titles"
        verbose_name = 'Titles'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=250, null=True)
    report_name = models.CharField(max_length=100, unique=True)
    services_map_code = models.CharField(max_length=30)
    service_deptname = models.ForeignKey(
        SubDepartments, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    method = models.CharField(max_length=30)
    service_order = models.IntegerField()
    report_format = models.IntegerField()
    is_suppress_report_name = models.BooleanField(default=True)
    service_footer = models.CharField(max_length=250, null=True)
    is_outside = models.BooleanField(default=True)
    is_print_together = models.BooleanField(default=True)
    is_web_flag = models.BooleanField(default=True)
    services_alias = models.CharField(max_length=30)
    services_days = models.IntegerField()
    is_critical_flag = models.BooleanField(default=True)
    is_sms_flag = models.BooleanField(default=True)
    color_code = models.CharField(max_length=30)
    sample_type = models.ForeignKey(
        Sampletype, on_delete=models.SET_NULL, null=True)
    disposal_day = models.IntegerField()
    gender_type = models.CharField(max_length=6) # TODO: query
    special_instruction = models.CharField(max_length=250, null=True)
    pat_instruction = models.CharField(max_length=250, null=True)
    tech_instruction = models.CharField(max_length=250, null=True)
    is_question_flag = models.BooleanField(default=True)
    is_urgent_flag = models.BooleanField(default=True)
    lab_process_time = models.IntegerField()
    urgent_process_time = models.IntegerField()
    is_consent_flag = models.BooleanField(default=True)
    services_status = models.CharField(max_length=1) # TODO: query
    is_services_for_home_collection = models.BooleanField(default=True)
    is_pdf_services = models.BooleanField(default=True)
    is_manual_services = models.BooleanField(default=True)
    is_gst_services = models.BooleanField(default=True)
    # creationid=models.CharField(max_length=200, null=True)
    created_on = models.DateTimeField(
        auto_created=True, default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "service"
        verbose_name = 'Service'
        verbose_name_plural = 'service'

    def __str__(self):
        return self.name

class Source(models.Model):
    name= models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)