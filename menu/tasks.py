# -*- coding:UTF-8 -*-
# import celery
import os,sys
import django
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weixin_app.settings')
django.setup()
from django.core.cache import cache
from chenxiang import models
from django.db.models.base import ModelBase
from menu.models import UserSmallAppMenus
from django.core.exceptions import ObjectDoesNotExist

from copy import copy


def get_value(obj,attr_names):
    value =copy(obj)
    for attr in attr_names.split('.'):
        value=getattr(value,attr,'')
    return value


# @celery.task
def get_latest_record(dirs):
    for table in dirs:
        cls = getattr(models,table)
        if isinstance(cls,ModelBase):
            if hasattr(cls,'editdate'):
                try:
                    obj1 = cls.objects.values().latest('editdate')
                    cache.set(cls._meta.label, obj1, timeout=60 * 60 * 24)
                    obj2 = cls.objects.latest('editdate')
                    menu=UserSmallAppMenus.objects.get(company_api_name=obj2._meta.label)
                    menu.value_formula = get_value(obj2,menu.value)
                    menu.subvalue_formula = get_value(obj2,menu.subvalue)
                    menu.subtitle_formula = get_value(obj2,menu.subtitle)
                    menu.save()

                except ObjectDoesNotExist:
                    continue


get_latest_record(dir(models))