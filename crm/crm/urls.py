
from django.contrib import admin
from django.urls import path
from web.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name = 'home'),
    path('our-clients/' , clients ,name = 'clients'),
    path('client-registration/',register ,name = 'register'),
    path('delete-client/<int:id>',delete_from_client ,name = 'delete_from_client'),
    path('account_logout/',logout,name='account_logout'),
    path('login/',loginPage,name='loginpage'),
    path('profile/<int:id>/',profile,name='profile'),
    path('messageform/<int:id>/',messageform,name='messageform'),
    path('statusform/<int:id>/',Statusform,name='statusform'),
    path('client_home/',client_home,name='client_home'),
    path('about/',about,name='about'),
    path('user_profile/',user_profile,name='user_profile'),
    path('delete_message/<int:id>',delete_message ,name = 'delete_message'),
    path('delete_status/<int:id>',delete_status ,name = 'delete_status'),

]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 