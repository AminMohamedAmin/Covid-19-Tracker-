from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='egy'),
    path('advice/',views.advice,name='advice'),
    path('question/',views.question,name='question'),
    path('contact/',views.contact,name='contact'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)