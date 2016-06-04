from django.db import models
from adminsortable.models import SortableMixin

HOW_IT_WORKS = 0
BATTLE = 1

FEATURE_TYPES = {
    HOW_IT_WORKS: 'how-it-works',
    BATTLE: 'battle'
}


class Feature(SortableMixin):

    class Meta:
        ordering = ['order']

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    type = models.IntegerField(choices=FEATURE_TYPES.items(), db_index=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image_url = models.CharField(max_length=128)

    def __unicode__(self):
        return u'{} ({})'.format(self.title, FEATURE_TYPES.get(self.type))


class FeatureVote(models.Model):
    email = models.EmailField(blank=True)
    feature = models.ForeignKey(Feature)
