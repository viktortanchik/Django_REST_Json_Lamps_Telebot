from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'lamps'
urlpatterns = [
    path('lamps/create/',LampsCreateView.as_view()),
    path('all', LampsListView.as_view()),
    path('lamps/detail/<int:pk>/', LampsDtailView.as_view())

]