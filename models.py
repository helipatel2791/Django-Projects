from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    user_password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'