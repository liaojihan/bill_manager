"""django_web URL Configuration

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
from django.conf.urls import url
from django_web.django_apps import home, bill

urlpatterns = [
    url(r'^home$', home.home),
    url(r'^user_login$', home.user_login),
    url(r'^forget$', home.forget),
    url(r'^user_add$', home.user_add),
    url(r'^bill$', bill.bill_init),
    url(r'^confirm_username$', home.confirm_username),
    url(r'^get_id_question', home.get_id_question),
    url(r'^check_answer$', home.check_answer),
    url(r'^reset_password$', home.reset_password),
    url(r'^reset_user_password$', home.reset_user_password)
]
