from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter),
    path('destroy_session', views.reset_counter),
    path('increment_by_two', views.add_by_2),
    path('custom_add_by_form', views.custom_add),
]