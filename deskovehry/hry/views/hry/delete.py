from django.shortcuts import get_object_or_404, redirect
from hry.models import DeskovaHra

def delete(request, hra_id):
    hra = get_object_or_404(DeskovaHra, id=hra_id)
    hra.delete()
    return redirect('seznam_her')
