from django.urls import re_path, path
from django.views.i18n import JavaScriptCatalog

from main import views

urlpatterns = [
    re_path(r'^task/$', views.home, name='home'),
    re_path(r'^mytask/$', views.mytask, name='mytask'),
    re_path(r'^addtask/$', views.addtask, name='addtask'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.doLogout, name='logout'),
    path('about/', views.about, name='about'),
]
