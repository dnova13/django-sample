from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    remove_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
