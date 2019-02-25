
from django.contrib import admin
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^results/$', views.search, name='search'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^invalid/', views.invalid, name='NOTlogin'),
    url(r'^goals/create/', views.create, name='create'),
    url(r'^goals/update/(?P<pk>\d+)/', views.update, name='update'),
    url(r'^goals/destroy/(?P<pk>\d+)/$', views.destroy, name='destroy'),
]