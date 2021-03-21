from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from .managers import FavoritesManager

from applications.entry.models import Entry

class Favorites(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Favorite Entry'
        verbose_name_plural = 'Favorites Entries'

    def __str__(self):
        return self.title