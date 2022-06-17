from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('profile/<str:username>/', views.profile, name='profile'), 
    path('update_profile/<str:username>/', views.update_profile, name='update-profile'), 
]  

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 