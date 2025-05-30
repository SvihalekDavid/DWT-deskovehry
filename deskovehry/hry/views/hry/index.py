from django.shortcuts import render
from hry.models import DeskovaHra

def index(request):
    hry = DeskovaHra.objects.all()
    context = { 'hry': hry }
    return render(request, 'hry/index.html', context)
