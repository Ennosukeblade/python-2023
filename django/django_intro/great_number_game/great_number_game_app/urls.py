from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('guess', views.guess),
    path('reset', views.delete_session),

]
