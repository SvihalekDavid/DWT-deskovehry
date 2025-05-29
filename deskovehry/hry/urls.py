from django.urls import path
from hry.views.hry.index import index

urlpatterns = [
    path('', index, name='seznam_her'),
]
