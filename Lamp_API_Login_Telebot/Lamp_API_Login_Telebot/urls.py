from django.contrib import admin
from django.urls import path, include
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/lamps/', include('lamps.urls')),
    path('', include('login.urls')),

]
