# -*- coding:UTF-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import os

from django.db import models
from treebeard.al_tree import AL_Node
from jsonfield import JSONField


class UserSmallAppMenus(AL_Node):
    name = models.CharField(max_length=100)
    company_id = models.IntegerField()
    company_api_name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    style = models.ForeignKey('SmallAppMenuStyle')
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    subvalue = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)
    icon_background = models.CharField(max_length=6)
    update_number = models.IntegerField(blank=True, null=True)
    is_top = models.IntegerField()
    is_dispaly = models.IntegerField()
    is_remind = models.IntegerField()
    create_timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    update_timestamp = models.DateTimeField(auto_now=True, editable=False)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True)
    sib_order = models.PositiveIntegerField()
    value_formula = models.CharField(max_length=100)
    subvalue_formula = models.CharField(max_length=100)
    subtitle_formula = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'UserSmallAppMenus'

    def __str__(self):
        return '%s%s' % ((self.get_depth() - 1) * '　', self.name)


class SmallAppMenuStyle(models.Model):
    name = models.CharField(max_length=100)
    script = JSONField()

    class Meta:
        managed = False
        db_table = 'SmallAppMenuStyle'

    def __str__(self):
        return self.name


class Companys(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    shorthand = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Companys'


class Usersmallappreportmenudata(models.Model):
    id = models.IntegerField(primary_key=True)
    report_menu = models.ManyToManyField('Usersmallappreportmenus')
    name = models.CharField(max_length=100, blank=True, null=True)
    data = JSONField()
    update_number = models.IntegerField()
    create_timestamp = models.DateTimeField()
    update_timestamp = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'UserSmallAppReportMenuData'


class Usersmallappreportmenurelation(models.Model):
    id = models.IntegerField(primary_key=True)
    report_menu = models.IntegerField()
    report_menu_data = models.IntegerField()
    date = models.DateTimeField()
    date_type = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'UserSmallAppReportMenuRelation'


class Usersmallappreportmenus(models.Model):
    company_id = models.IntegerField()
    user_id = models.IntegerField()
    style_id = models.IntegerField()
    name = models.CharField(max_length=100)
    is_top = models.IntegerField()
    is_display = models.IntegerField()
    is_remind = models.IntegerField()
    update_number = models.IntegerField()
    create_timestamp = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'UserSmallAppReportMenus'


class CubesModel(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）', unique=True)
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    description = models.CharField(max_length=255, help_text='描述（可选）', null=True)
    store = models.CharField(max_length=100, help_text='存储（可选）', null=True)
    mappings = JSONField(null=True, help_text='对应关系（可选）')
    joins = JSONField(null=True, help_text='连接关系（可选）')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class Cube(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）', unique=True)
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    description = models.CharField(max_length=255, help_text='描述（可选）', null=True)
    key = models.CharField(max_length=100, null=True, help_text='主键字段（可选）')
    fact = models.CharField(max_length=100, null=True, help_text='指定数据库表名称，如果不指定，以名称匹配')
    model = models.ForeignKey('CubesModel', related_name='cubes', help_text='选择所属模型')
    dimensions = models.ManyToManyField('Dimension', related_name='cubes')
    mappings = JSONField(null=True, help_text='对应关系（可选）')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class Dimension(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）', unique=True)
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    description = models.CharField(max_length=255, help_text='描述（可选）', null=True)
    model = models.ForeignKey('CubesModel', related_name='dimensions')
    role = models.CharField(max_length=10, help_text='角色（可选）', null=True)
    default_hierarchy_name = models.CharField(max_length=100, help_text='默认层（可选）', null=True)
    alias = models.CharField(max_length=100, help_text='数据库字段名称（可选）', null=True)
    cardinality = models.CharField(max_length=10, choices=(
        ('tiny', '0-5'), ('low', '5-50'), ('medium', '>50'), ('high', 'may refuse')), null=True, help_text='维的数量范围（可选）')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class Measure(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    cube = models.ForeignKey('Cube', related_name='measures')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class Aggregate(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    measure = models.ForeignKey('Measure', related_name='aggregates', null=True)
    cube = models.ForeignKey('Cube', related_name='aggregates')
    function = models.CharField(choices=(('count', '计数'), ('sum', '求和'), ('min', '最小'), ('max', '最大'), ('avg', '求平均')),
                                help_text='汇聚方法', max_length=10, null=True)
    expressions = models.CharField(max_length=255, null=True, help_text='计算表达式，如:sum(measure)')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class Hierarchy(models.Model):
    dimension = models.ForeignKey('Dimension', related_name='hierarchies')
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class DimensionLevel(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    dimension = models.ForeignKey('Dimension', related_name='levels')
    key = models.CharField(max_length=50, help_text='key field of the level', null=True)
    label_attribute = models.CharField(max_length=50, help_text='name of attribute containing label to be displayed',
                                       null=True)
    order_attribute = models.CharField(max_length=50, help_text='name of attribute that is used for sorting',
                                       null=True)
    cardinality = models.CharField(max_length=10, choices=(
        ('tiny', '0-5'), ('low', '5-50'), ('medium', '>50'), ('high', 'may refuse')), null=True, help_text='级的数量范围（可选）')
    role = models.CharField(max_length=10, help_text='角色（可选）', null=True)

    def __str__(self):
        return self.name


class HierarchyLevel(models.Model):
    hierarchy = models.ForeignKey('Hierarchy', related_name='levels')
    name = models.ForeignKey('DimensionLevel', help_text='名称（必填）', db_column='name')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    key = models.CharField(max_length=50, help_text='key field of the level', null=True)
    label_attribute = models.CharField(max_length=50, help_text='name of attribute containing label to be displayed',
                                       null=True)
    order_attribute = models.CharField(max_length=50, help_text='name of attribute that is used for sorting',
                                       null=True)
    cardinality = models.CharField(max_length=10, choices=(
        ('tiny', '0-5'), ('low', '5-50'), ('medium', '>50'), ('high', 'may refuse')), null=True)
    role = models.CharField(max_length=10, help_text='角色（可选）', null=True)

    def __str__(self):
        return getattr(self.name, 'name', '')


class DimensionAttribute(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    dimension = models.ForeignKey('Dimension', related_name='attributes')
    order = models.CharField(max_length=5, choices=(('asc', '升序'), ('desc', '降序')), null=True)
    missing_value = models.CharField(max_length=100, null=True, help_text='替换空值')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class HierarchyAttribute(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    label = models.CharField(max_length=100, help_text='标签（可选）', null=True)
    level = models.ForeignKey('HierarchyLevel', related_name='attributes')
    order = models.CharField(max_length=5, choices=(('asc', '升序'), ('desc', '降序')), null=True)
    missing_value = models.CharField(max_length=100, null=True, help_text='替换空值')

    def __str__(self):
        return '%s:%s'%(self.id,self.name)


class SaveToModelFile(models.Model):
    config = models.ForeignKey('CubesModel', help_text='（必填）选择要保存的配置文件')
    path = models.CharField(max_length=255,
                            help_text='（可选）cube配置文件路径。该路径下必须存在slicer.ini配置文件。配置后，从该路径的_model文件夹中加载json文件。如不了解，不要填写',
                            default=r'/www/wwwroot/cubes_define')
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.path = os.path.join(os.path.join(self.path, '_models'),self.config.name + '.json')
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)


class CubeJoin(models.Model):
    name = models.CharField(max_length=100, help_text='名称（必填）')
    cube = models.ForeignKey('Cube', related_name='joins')
    master = models.CharField(max_length=100, help_text='主表表达式,一般是量表的某个外键ID,格式：fact_sales.product_id')
    detail = models.CharField(max_length=100, help_text='细表表达式,一般是维表的主键ID，格式：dim_product.key')
    method = models.CharField(help_text='（可选）匹配方法', choices=(('match', '内连接（默认）'), ('detail', '细外连接'), ('master', '主外连接')),
                              null=True,max_length=12)
    alias = models.CharField(help_text='（可选）What if you need to join same table twice or more times', null=True, max_length=50)

    def __str__(self):
        return '%s:%s'%(self.id,self.name)