from django.shortcuts import render
# from hry.models import DeskovaHra

def index(request):
    # hry = DeskovaHra.objects.all()
    return render(request, 'hry/index.html')
