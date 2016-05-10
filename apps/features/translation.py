from modeltranslation.translator import translator, TranslationOptions
from apps.features.models import Feature


class FeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Feature, FeatureTranslationOptions)
