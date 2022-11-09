from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from accounts.models import User

from core_api.models import Doctor, Source

# Create your models here.

class Patient (models.Model):

    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ]

    patient_id = models.BigIntegerField()
    title=models.CharField(max_length=10)
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=False)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='m', unique=True)
    age = models.IntegerField()
    dob = models.DateField()
    patient_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.BigIntegerField()
    status = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    nationality = models.IntegerField()
    passport_no = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    last_visit_date = models.DateField(null=True)

class Visit(models.Model):
    visit_id = models.BigIntegerField(),
    patient_id = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    visit_no = models.CharField(max_length=100)
    visit_date = models.DateField(),
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    source_id = models.ForeignKey(Source,  on_delete=models.SET_NULL, null=True)
    bill_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    total_rate = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    other_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    discount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    balance = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    receipt_no = models.CharField(max_length = 100)
    complete_flag = models.BooleanField(default=False)
    ref_number = models.CharField(max_length=255)
    dispatch_mode = models.CharField(max_length=1)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invalid_flag = models.IntegerField()
    consumable_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    refund_amount =models.DecimalField(null=True, max_digits=20, decimal_places=2)
    visit_time = models.TimeField()
    bill_number = models.IntegerField()
    age_in_days = models.IntegerField()
    registration_code = models.IntegerField()
    sms_repost = models.BooleanField(default=False)
    web_repost = models.BooleanField(default=False)
    hard_copy_repost = models.BooleanField(default=False)
