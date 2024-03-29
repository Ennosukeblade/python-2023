from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs/', views.index, name='index'),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/destroy/', views.destroy),
    path('blogs/json/', views.json_res),
]