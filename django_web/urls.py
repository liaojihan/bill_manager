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
from django_web.django_apps import home, bill, type

urlpatterns = [
    url(r'^home$', home.home, name='home'),
    url(r'^user_login$', home.user_login, name='user_login'),
    url(r'^logout$', home.logout, name='logout'),
    url(r'^forget$', home.forget, name='forget'),
    url(r'^user_add$', home.user_add, name='user_add'),
    url(r'^confirm_username$', home.confirm_username, name='confirm_username'),
    url(r'^get_id_question', home.get_id_question, name='get_id_question'),
    url(r'^check_answer$', home.check_answer, name='check_answer'),
    url(r'^reset_password$', home.reset_password, name='reset_password'),
    url(r'^reset_user_password$', home.reset_user_password, name='reset_user_password'),
    url(r'^bill$', bill.bill, name='bill'),
    url(r'^detailed$', bill.detailed, name='detailed'),
    url(r'^get_table_data$', bill.get_table_data, name='get_table_data'),
    url(r'^get_type$', type.get_type, name='get_type'),
    url(r'^bill_data_add$', bill.bill_data_add, name='bill_data_add'),
    url(r'^bill_data_delete$', bill.bill_data_delete, name='bill_data_delete'),
    url(r'^type_add$', type.type_add, name='type_add'),
    url(r'^get_detailed$', bill.get_detailed, name='get_detailed'),
    url(r'^edit_bill$', bill.edit_bill, name='edit_bill'),
    url(r'^get_edit_type$', type.get_edit_type, name='get_edit_type'),
    url(r'^update_bill$', bill.update_bill, name='update_bill'),
    url(r'^search_bill$', bill.search_bill, name='search_bill'),
    url(r'^get_overview_data$', bill.get_overview_data, name='get_overview_data'),
    url(r'^reload_area_charts', bill.reload_area_charts, name='reload_area_charts')
]
