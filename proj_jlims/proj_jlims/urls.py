
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('app_jlims.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('api_jlims.urls')),
]
