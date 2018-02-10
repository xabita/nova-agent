from django.conf.urls import include, url
from users import views as user_views
#from django.contrib.auth import views as auth_views


urlpatterns = [

    #url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^users/$', user_views.home, name='home'),    
    

   ]

