"""weixin_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from menu.views import ObtainExpireAuthToken

router = DefaultRouter()
router.register(r'token',ObtainExpireAuthToken,base_name='token')

extra_pattern=[
    url(r'^supermarket/',include('chenxiang.urls'),name='supermarket')
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^company/',include(extra_pattern,namespace='company')),
    url(r'^menu/',include('menu.urls',namespace='menu')),
    url(r'^upload/',include('upload.urls',namespace='upload')),
    url(r'^docs/',include_docs_urls(title='API Document')),
    url(r'^open/',include(router.urls,namespace='open'),)
]
