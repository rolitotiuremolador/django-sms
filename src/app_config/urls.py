from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from sms_app import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('elements/<int:pk>/', views.element_processes, name='element_processes'),
    # url(r'^elements/(?P<pk>\d+)/$', views.element_processes, name='element_processes' ), 
    path('elements/<int:pk>/new/', views.new_process, name = "new_process"),
]
