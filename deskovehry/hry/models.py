from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class DeskovaHra(models.Model):
    nazev = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3, "Název musí mít alespoň 3 znaky.")],
        verbose_name=_("Název hry"),
        help_text=_("Zadejte název deskové hry.")
    )
    popis = models.TextField(
        blank=True,
        verbose_name=_("Popis"),
        help_text=_("Krátký popis hry.")
    )
    datum_vydani = models.DateField(
        verbose_name=_("Datum vydání")
    )
    cena = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_("Cena")
    )
    pocet_hracu = models.IntegerField(
        verbose_name=_("Počet hráčů")
    )
    datum_pridani = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nazev
