from django.urls import path
from . import views
urlpatterns = [
    path('', views.page_1),
    path('login', views.index),
    path('setup_lamp', views.setup_lamp),
    path('contact', views.contact),
    path('products', views.products),


]
