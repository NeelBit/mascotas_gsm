from django.urls import path, include
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls'), name="accounts"),
    path('logout', LogoutView.as_view(), name="logout"),
]

# error 404
from django.conf.urls import handler404
from .views import mi_error_404

handler404 = mi_error_404
#handler404 = 'views.mi_error_404'