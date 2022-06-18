from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),   

    path('profile/<str:username>/', views.profile, name='profile'), 
    path('update_profile/<str:username>/', views.update_profile, name='update-profile'), 

    path('create-hood/', views.create_hood, name='create-hood'),
    path('view-hood/<int:hood_id>/', views.view_hood, name='view-hood'),
    path('<int:hood_id>/residents/', views.hood_residents, name='hood-residents'),

    path('join_hood/<int:id>/', views.join_hood, name='join-hood'),
    path('leave_hood/<int:id>/', views.leave_hood, name='leave-hood'),

    path('post-business/<int:hood_id>/', views.post_a_business, name='post-business'),
    path('search-business/', views.search_business, name='search-business'),
    path('create-update/<int:hood_id>/', views.create_hood_update, name='create-update'), 
]  

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 