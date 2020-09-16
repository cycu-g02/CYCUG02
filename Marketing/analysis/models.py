from django.db import models

# Create your models here.

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
