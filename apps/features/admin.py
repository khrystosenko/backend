from django.contrib import admin
from adminsortable.admin import SortableAdmin
from modeltranslation.admin import TranslationAdmin
from apps.features.models import Feature


class FeatureAdmin(SortableAdmin, TranslationAdmin):
    pass


admin.site.register(Feature, FeatureAdmin)

