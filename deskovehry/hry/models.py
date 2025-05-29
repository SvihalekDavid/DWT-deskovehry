from django.db import models
from django.core.validators import MinLengthValidator

class DeskovaHra(models.Model):
    nazev = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3, "Název musí mít alespoň 3 znaky.")],
        verbose_name="Název hry"
    )
    popis = models.TextField(
        blank=True,
        verbose_name="Popis",
        help_text="Krátký popis hry (volitelné)."
    )
    datum_vydani = models.DateField(
        verbose_name="Datum vydání"
    )
    cena = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Cena (Kč)"
    )
    pocet_hracu = models.IntegerField(
        verbose_name="Počet hráčů"
    )
    datum_pridani = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nazev
