from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class Presentation(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    #slides = ListField(EmbeddedModelField(Slide)) <-- Best Implementation

    def __unicode__(self):
        return "Presentation %s" % self.name


class Slide(models.Model):
    index = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    presentation = models.ForeignKey(Presentation, db_index=True)

    class Meta:
        unique_together = (('title', 'presentation'),)

    def __unicode__(self):
        return "Slide: %s" % (self.title)
