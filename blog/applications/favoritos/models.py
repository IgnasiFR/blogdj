from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings

from applications.entrada.models import Entry

# Create your models here.

class Favorites(TimeStampedModel):
    """Modelo para favoritos"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "user_favorites", on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name = "entry_favorites", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','entry')
        verbose_name = "Entrada favorita"
        verbose_name_plural = "Entradas favoritas"

    def __ster__(self):
        return self.entry.title



