from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('department/', views.department, name='department'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
