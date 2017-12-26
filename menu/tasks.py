# -*- coding:UTF-8 -*-
# import celery
# import os,sys
# import django
# sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weixin_app.settings')
# django.setup()
from django.core.cache import cache
from chenxiang import models
from django.db.models.base import ModelBase
from menu.models import UserSmallAppMenus
from django.core.exceptions import ObjectDoesNotExist
import celery


def get_value(obj,attrs):
    if attrs[0]:
        if len(attrs) ==1:
            return getattr(obj,attrs[0],None)
        else:
            try:
                new_obj = getattr(obj,attrs[0])
                return get_value(new_obj,attrs[1:])
            except AttributeError:
                return


@celery.task
def get_latest_record(dirs):
    for table in dirs:
        cls = getattr(models,table)
        if isinstance(cls,ModelBase):
            try:
                if hasattr(cls,'editdate'):
                    obj1 = cls.objects.values().latest('editdate')
                    obj2 = cls.objects.latest('editdate')
                else:
                    obj2 = cls.objects.order_by('-'+cls._meta.pk.attname).first()
                    obj1 = cls.objects.order_by('-'+cls._meta.pk.attname).values().first()
                if not obj1:
                    continue
                cache.set(cls._meta.label, obj1, timeout=60 * 60 * 24)

                menu=UserSmallAppMenus.objects.get(company_api_name=obj2._meta.label)
                menu.value = get_value(obj2,menu.value_formula.split('.'))
                menu.subvalue = get_value(obj2,menu.subvalue_formula.split('.'))
                menu.subtitle = get_value(obj2,menu.subtitle_formula.split('.'))
                menu.save()

            except ObjectDoesNotExist:
                continue


get_latest_record(dir(models))