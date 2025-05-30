from django import forms
from hry.models import DeskovaHra
import bleach
from django.utils.translation import gettext_lazy as _

class DeskovaHraForm(forms.ModelForm):
    class Meta:
        model = DeskovaHra
        fields = ['nazev', 'popis', 'datum_vydani', 'cena', 'pocet_hracu']
        labels = {
            'nazev': _("Název hry"),
            'popis': _("Popis"),
            'datum_vydani': _("Datum vydání"),
            'cena': _("Cena"),
            'pocet_hracu': _("Počet hráčů"),
        }
        help_texts = {
            'nazev': _("Zadejte název hry s minimálně 3 znaky."),
        }
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control', 'minlength': '3'}),
            'popis': forms.Textarea(attrs={'class': 'form-control'}),
            'datum_vydani': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cena': forms.NumberInput(attrs={'class': 'form-control'}),
            'pocet_hracu': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_popis(self):
        content = self.cleaned_data.get('popis')
        return bleach.clean(content, tags=bleach.sanitizer.ALLOWED_TAGS, strip=True)
