from __future__ import unicode_literals

from django.db import models

import json


class KeyValueSettingManager(models.Manager):
    def get_value(self, key):
        setting = super(KeyValueSettingManager, self).get_queryset().get(key=key)
        return setting.value

    def get_dict_value(self, key):
        setting = super(KeyValueSettingManager, self).get_queryset().get(key=key)
        return json.loads(setting.value)


class KeyValueSetting(models.Model):
    key = models.CharField(
        unique=True,
        max_length=255)
    value = models.TextField()
    notes = models.TextField(
        blank=True)
    added_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    objects = KeyValueSettingManager()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'key value setting'
        verbose_name_plural = 'key value settings'
