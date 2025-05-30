from django.shortcuts import render
from hry.forms.uzivatele.nick_form import NickForm

def set_nick(request):
    form = NickForm(request.POST or None)
    context = {
        'formular': form,
    }

    if request.method == 'POST' and form.is_valid():
        nick = form.cleaned_data['username']
        request.session['nick'] = nick  # uložíme přezdívku do session
    context['nick'] = request.session.get('nick', None)

    return render(request, 'uzivatele/nick_zmenit.html', context)
