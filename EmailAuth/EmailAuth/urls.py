
from django.contrib import admin
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^logout/', views.logout, name='logout'),
]