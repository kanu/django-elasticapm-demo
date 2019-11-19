from django.db import models


class LinkItem(models.Model):
    url = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    position = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.label
