from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='home'),
    path('contact/', views.contact_view, name='contact'),

    #path('result/',views.contact_view, name='result' )
]