from django.urls import path
from hry.views.hry.index import index
from hry.views.hry.delete import delete
from hry.views.hry.create import vytvorit
from hry.views.hry.edit import upravit
from hry.views.uzivatele.nastav import set_nick

urlpatterns = [
    path('', index, name='seznam_her'),
    path('<int:hra_id>/smazat/', delete, name='smazat_hru'),
    path('nick/', set_nick, name='uzivatel_nick'),
    path('pridat/', vytvorit, name='pridat_hru'),  # nová routa
    path('<int:hra_id>/upravit/', upravit, name='upravit_hru'),
]
