from django.urls import path
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ...
    path('accounts/', include('django.contrib.auth.urls')),
    # ...
]
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [

]