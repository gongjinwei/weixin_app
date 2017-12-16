# -*- coding:UTF-8 -*-
from import_export import resources
from . import models

class CubesModelResources(resources.ModelResource):
    class Meta:
        model = models.CubesModel
        exclude = ('id',)