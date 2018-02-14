from django.conf.urls import include, url
from users import views as user_views
#from django.contrib.auth import views as auth_views


urlpatterns = [

    #url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^users/$', user_views.home, name='home'),
    url(r'^users/new/$', user_views.users_new, name='users_new'),
    url(r'^users/add/$', user_views.users_add, name='users_add'),
    url(r'^profile/(?P<pk>[0-9]+)/$', user_views.users_profile, name='users_profile'),
     
    

   ]

