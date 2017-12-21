# -*- coding:UTF-8 -*-
from rest_framework.renderers import BrowsableAPIRenderer
from django.contrib.auth.views import LoginView


class APIRenderer(BrowsableAPIRenderer):
    template = 'customer_api.html'


