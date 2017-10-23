from hello import views
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from hello import views as hello_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views

from django.conf import settings
from blog import views as blog_views
from .settings import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [

    # static about contact
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index),
	url(r'^$', hello_views.get_index, name='index'),
    url(r'^contact/$', views.get_contact, name='contact'),
    url(r'^contact_thanks/$', views.get_contact_thanks, name='contact_thanks'),
    url(r'^about/$', hello_views.get_About, name='about'),

    # accounts
	url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),



    # paypal URLs
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    url(r'^products/$', hello_views.get_products, name='products'),
    url(r'^paypal_cancel/$', hello_views.get_paypal_cancel, name='paypal_cancel'),
    url(r'^paypal_return/$', hello_views.get_paypal_return, name='paypal_return'),


    # Blog URLs
    url(r'^blog/$', blog_views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))