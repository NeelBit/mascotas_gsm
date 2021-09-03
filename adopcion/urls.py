from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('adoptar/', views.adopta, name='adopta'),
    path('poner-adopcion/', views.poner_adopcion, name='poner_adopcion'),
    path('adoptar/perros', views.perros, name='perros'),
    path('adoptar/gatos', views.gatos, name='gatos'),
    path('adoptar/otros', views.otros, name='otros'),
    #adoptar/<int:id> para post detail
    path('adoptar/<int:pk>', views.post_detail_view, name='post_detail'),
]
