from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from azbankgateways.urls import az_bank_gateways_urls
from payments.views import go_to_gateway_view, callback_gateway_view

admin.autodiscover()

urlpatterns = [
    path('bankgateways/', az_bank_gateways_urls()),

    path('callback-gateway-view/', callback_gateway_view),

    path('go-to-gateway/', go_to_gateway_view, name='process'),

    path('payments/',include('payments.urls')),

]



urlpatterns += [
    path('admin/', admin.site.urls),
    path('acc/', include('profiles.urls')),
    path('',include('products.urls')),
    path('pages/',include('pages.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('accounts/',include('allauth.urls')),
    path('process/',include('process.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
