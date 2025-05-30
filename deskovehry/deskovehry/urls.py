from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),             # Homepage
    path('hry/', include('hry.urls')),              # Seznam her
    path('admin/', admin.site.urls),               # Admin
]

