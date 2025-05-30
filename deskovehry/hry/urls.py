from django.urls import path
from hry.views.hry.index import index
from hry.views.hry.delete import delete
from hry.views.uzivatele.nastav import set_nick

urlpatterns = [
    path('', index, name='seznam_her'),
    path('<int:hra_id>/smazat/', delete, name='smazat_hru'),
    path('nick/', set_nick, name='uzivatel_nick'),  # nová routa
]
