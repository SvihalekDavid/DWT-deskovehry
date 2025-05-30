from django.shortcuts import render, get_object_or_404, redirect
from hry.models import DeskovaHra
from hry.forms.hry.deskova_hra_form import DeskovaHraForm

def upravit(request, hra_id):
    hra = get_object_or_404(DeskovaHra, id=hra_id)

    if request.method == 'POST':
        form = DeskovaHraForm(request.POST, instance=hra)
        if form.is_valid():
            form.save()
            return redirect('seznam_her')
    else:
        form = DeskovaHraForm(instance=hra)

    return render(request, 'hry/create.html', {
        'form': form,
        'hra': hra
    })
