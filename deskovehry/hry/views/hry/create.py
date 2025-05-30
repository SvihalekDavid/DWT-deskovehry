from django.shortcuts import render, redirect
from hry.forms.hry.deskova_hra_form import DeskovaHraForm

def vytvorit(request):
    if request.method == 'POST':
        form = DeskovaHraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seznam_her')
    else:
        form = DeskovaHraForm()

    return render(request, 'hry/create.html', { 'form': form })
