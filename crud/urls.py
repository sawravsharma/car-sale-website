from django.conf.urls import url, re_path
from . import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
	url(r'^log$', views.log, name='log'),
	url(r'^paybill$', views.paybill, name='paybill'),
	url(r'^login$', views.login, name='login'),
	url(r'^pro$', views.pro, name='pro'),
	url(r'^pview$', views.pview, name='pview'),
	url(r'^sign$', views.sign, name='sign'),
	url(r'^signup$', views.signup, name='signup'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^pcreate$', views.pcreate, name='pcreate'),
	url(r'^addbill$', views.addbill, name='addbill'),
    url(r'^pdelete/(?P<id>\d+)$', views.pdelete, name='pdelete'),
    url(r'^pcart/(?P<id>\d+)$', views.pcart, name='pcart'),
    url(r'^scart/(?P<id>\d+)$', views.scart, name='scart'),
	url(r'^pcartdelete/(?P<id>\d+)$', views.pcartdelete, name='pcartdelete'),
    url(r'^viewcart$', views.viewcart, name='viewcart'),
    url(r'^show_cars$', views.show_cars, name='show_cars')
]