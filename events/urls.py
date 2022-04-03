from django.urls import path
from . import views


urlpatterns = [
    path('fetch-event', views.get_events, name='get_events'),
    path('delete-event/<int:pk>', views.delete_event, name='delete_event'),
    path('update-event/<int:pk>', views.update_event, name='update_event'),
    path('create-event', views.create_event, name='create_event'),
    path('yearwise-event/<int:year>', views.get_events_yearwise, name='get_events_yearwise')
]
