from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Repo import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('add', views.add, name='add'),
    path('resources', views.resources, name='resources'),
    path('confirm/<str:token>', views.confirm, name='confirm'),
    path('delete/<str:token>', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)