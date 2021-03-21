#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ), 
    path(
        'suscription-record', 
        views.SubcriberCreateView.as_view(),
        name='add-suscription',
    ),  
    path(
        'rcontact', 
        views.ContactCreateView.as_view(),
        name='add-contact',
    ),  
]