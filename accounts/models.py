from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from dateutil.relativedelta import relativedelta

from accounts.choices import GENDER_DICT, GenderTypeChoices


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        """
        Create and save a user with the given username and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, TimeStampedModel):
    username = models.CharField(max_length=200, unique=True)
    guid = models.UUIDField(default=uuid.uuid4, unique=True)
    contact_number = models.CharField(max_length=200, unique=True)
    email = models.EmailField(null=True, blank=True)
    image = models.URLField(null=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "account_users"
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def roles(self):
        return [group.name for group in self.groups.all()]


class UserProfile(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_profile")
    guid = models.UUIDField(default=uuid.uuid4, unique=True)
    contact_number = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.PositiveIntegerField(
        choices=GenderTypeChoices.choices, null=True)
    dob = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_profile"
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'

    def __str__(self):
        return self.first_name or ''

    def get_age(self):
        _current_date = datetime.now().date()
        if self.dob:
            return relativedelta(_current_date, self.dob).years
        return None

    @property
    def gender_text(self):
        if self.gender:
            return GENDER_DICT.get(self.gender)
        return ""

    @property
    def full_name(self):
        try:
            if self.middle_name:
                name_list = [self.first_name, self.middle_name, self.last_name]
            elif self.last_name:
                name_list = [self.first_name, self.last_name]
            else:
                name_list = [self.first_name]
            return " ".join(name_list)
        except:
            return " "

    def update_data_points(self, response):
        for extracted_item in response.get('result'):
            if 'details' in extracted_item and 'name' in extracted_item.get('details'):
                self.first_name = extracted_item.get(
                    'details').get('name').get('value').split()[0]
                self.last_name = extracted_item.get(
                    'details').get('name').get('value').split()[-1]
            # todo: maintain versions of extractors as json schema and validate with the same before manipulating.

            if 'details' in extracted_item and 'gender' in extracted_item.get('details'):
                self.gender = 1 if extracted_item.get('details').get(
                    'gender').get('value') == 'MALE' else 2

            self.save()
        return None
