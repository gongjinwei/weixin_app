from django.db import models
from jsonfield import JSONField

# Create your models here.


class Create(models.Model):
    id = models.CharField(primary_key=True,help_text='主键',max_length=42,editable=False)
    last_state = models.CharField(max_length=50,help_text='上一次更新状态',)
    dept_no = models.CharField(max_length=50,help_text='机构号')
    database_name = models.CharField(max_length=50,help_text='数据库类型:数据库名称')
    table_name = models.CharField(max_length=50,help_text='表名称')
    create_time=models.DateTimeField(auto_now_add=True,editable=False)
    update_time=models.DateTimeField(auto_now=True,editable=False)
    key=models.CharField(max_length=100,default='')
    data = JSONField(editable=False)
