from django.db import models
from jsonfield import JSONField

# Create your models here.


class Create(models.Model):
    id = models.CharField(primary_key=True,help_text='主键',max_length=42,editable=False)
    version = models.IntegerField(help_text='当前版本号',default=0,editable=False)
    last_version = models.IntegerField(help_text='上一次的版本号,新建的版本号为-1')
    last_state = models.CharField(max_length=50,help_text='上一次更新状态')
    dept_no = models.CharField(max_length=50,help_text='机构号')
    database_name = models.CharField(max_length=50,help_text='数据库类型:数据库名称')
    table_name = models.CharField(max_length=50,help_text='表名称')
    key_str = models.CharField(max_length=255,help_text='唯一标识字符串')
    data = JSONField()
