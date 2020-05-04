#made by @M0M
#from django.conf.urls import url we don't work with urls but path
#from django.contrib import admin admin is not needed
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name='aboutUs'),
    path('contact/', views.contact, name='contactUs'),
    path('tracker/', views.tracker, name='trackingStatus'),
    path('search/', views.search, name='search'),
    path('productView', views.productView, name='productView'),
    path('checkout/', views.checkout, name='checkout'),
]
