
from django.db import models


class Users(models.Model):

    user_id = models.IntegerField(primary_key=True)
    user_first_name = models.CharField(max_length=255, null=False)
    user_last_name = models.CharField(max_length=255, null=False)
    user_age = models.IntegerField(null=False)
    user_birth_date = models.DateField(null=False)
    user_gender = models.CharField(max_length=255, null=False)
    user_email = models.CharField(max_length=255, null=False)
    user_phone = models.CharField(max_length=255, null=False)
    user_cell = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'users'


class UsersLogin(models.Model):

    user_login_id = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        related_name='user_login',
        primary_key=True,
        db_column='user_login_id'
    )
    user_uuid = models.CharField(max_length=255, null=False)
    user_username = models.CharField(max_length=255, null=False)
    user_password = models.CharField(max_length=255, null=False)
    user_salt = models.CharField(max_length=255, null=False)
    user_md5 = models.CharField(max_length=255, null=False)
    user_sha1 = models.CharField(max_length=255, null=False)
    user_sha256 = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'users_login'


class UsersAddresses(models.Model):
    user_address_id = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        related_name='user_address',
        primary_key=True,
        db_column='user_address_id'
    )
    user_street_name = models.CharField(max_length=255, null=False)
    user_street_number = models.IntegerField(null=False)
    user_city = models.CharField(max_length=255, null=False)
    user_state = models.CharField(max_length=255, null=False)
    user_country = models.CharField(max_length=255, null=False)
    user_postcode = models.CharField(max_length=255, null=False)
    user_latitude = models.CharField(max_length=255, null=False)
    user_longitude = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'users_addresses'

