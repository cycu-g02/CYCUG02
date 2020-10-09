from django.db import models

# Create your models here.
class SiteNote(models.Model):
    ENABLE = '1'# 預設啟用
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    eng_name = models.CharField(max_length=60, null=True)
    url = models.CharField(max_length=60, null=True)
    parent_id = models.IntegerField(default=0)
    enable = models.CharField(max_length=1, default=ENABLE)
    idx = models.IntegerField(default=99)
    data_feather = models.CharField(max_length=30, null=True)

class Category(models.Model):
    ENABLE = '1'  # 預設啟用
    super_parent_id = 0
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=60, null=True)
    parent_id = models.IntegerField(default=0)
    enable = models.CharField(max_length=1, default=ENABLE)
    idx = models.IntegerField(default=99)
    def set_super_parent_id(self, super_parent_id):
        self.super_parent_id = super_parent_id

    def get_super_parent_id(self):
        return self.super_parent_id

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=30)
    picture = models.CharField(max_length=60)

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=30)
    ltime = models.DateTimeField(auto_now=True)

