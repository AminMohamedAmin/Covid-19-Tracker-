from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name='home'),
	path('country_info/',views.Country_Info,name='country_info'),
	path('country_history/',views.Country_History,name='country_history'),
	path('assurance/',views.Assurance,name='assurance'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)