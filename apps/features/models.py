from django.db import models
from adminsortable.models import SortableMixin

FEATURE_TYPES = (
    (0, 'how-it-works'),
    (1, 'battle')
)

def get_feature_type(value):
    for i, title in FEATURE_TYPES:
        if i == value: return title


class Feature(SortableMixin):

    class Meta:
        ordering = ['order']

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    type = models.IntegerField(choices=FEATURE_TYPES, db_index=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image_url = models.CharField(max_length=128)


    def __str__(self):
        return '{} ({})'.format(self.title, get_feature_type(self.type))
