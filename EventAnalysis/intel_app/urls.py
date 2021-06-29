from django.urls import path
from . import views

urlpatterns = [
    path('', views.intel_index),
    path('group/create', views.create_group),
    path('event/create', views.create_event),
    path('group/<int:group_id>', views.group_page),
    path('event/<int:event_id>', views.event_page),
    path('group/<int:group_id>/delete', views.destroy_group),
    path('event/<int:event_id>/delete', views.destroy_event)
    
]