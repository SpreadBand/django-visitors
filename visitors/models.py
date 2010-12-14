from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Visit(models.Model):
    when = models.DateTimeField(_('when'), auto_now_add=True)
    
    # Who visited
    visitor_content_type = models.ForeignKey(ContentType, related_name='visited_objects')
    visitor_object_id = models.PositiveIntegerField(db_index=True)
    visitor = generic.GenericForeignKey('visitor_content_type', 'visitor_object_id')

    # Who was visited
    visited_content_type = models.ForeignKey(ContentType, related_name='latest_visitors')
    visited_object_id = models.PositiveIntegerField(db_index=True)
    visited = generic.GenericForeignKey('visited_content_type', 'visited_object_id')










