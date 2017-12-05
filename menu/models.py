# -*- coding:UTF-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from treebeard.al_tree import AL_Node
from jsonfield import JSONField


class UserSmallAppMenus(AL_Node):
    name = models.CharField(max_length=100)
    company_id = models.IntegerField()
    company_api_name=models.CharField(max_length=50)
    user_id = models.IntegerField()
    style = models.ForeignKey('SmallAppMenuStyle')
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=50)
    value = models.FloatField()
    subvalue = models.FloatField()
    image = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)
    icon_background = models.CharField(max_length=6)
    update_number = models.IntegerField(blank=True, null=True)
    is_top = models.IntegerField()
    is_dispaly = models.IntegerField()
    is_remind = models.IntegerField()
    create_timestamp = models.DateTimeField(auto_now_add=True,editable=False)
    update_timestamp = models.DateTimeField(auto_now=True,editable=False)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True)
    data = JSONField()
    sib_order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table='UserSmallAppMenus'

    def __str__(self):
        return '%s%s' % ((self.get_depth() - 1) * '　', self.name)


class SmallAppMenuStyle(models.Model):
    name = models.CharField(max_length=100)
    script=JSONField()

    class Meta:
        managed = False
        db_table='SmallAppMenuStyle'

    def __str__(self):
        return self.name





