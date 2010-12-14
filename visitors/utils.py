from datetime import datetime, timedelta

from django.contrib.contenttypes.models import ContentType

from .models import Visit

def record_visit(visitor, visited, timeout=3600):
    """
    Record a new visit or update an existing one if newer than timeout
    (in seconds)
    """
    visitor_ctype = ContentType.objects.get_for_model(visitor)
    visited_ctype = ContentType.objects.get_for_model(visited)

    time_limit = datetime.now() - timedelta(seconds=timeout)

    try:
        visit = Visit.objects.get(visitor_content_type=visitor_ctype,
                                  visitor_object_id=visitor.pk,
                                  visited_content_type=visited_ctype,
                                  visited_object_id=visited.pk,
                                  when__gt=time_limit)
        
        # If we have a record, then update its time
        visit.when = datetime.now()
        visit.save()

        return visit

    except Visit.DoesNotExist, e:
        return Visit.objects.create(visitor_content_type=visitor_ctype,
                                    visitor_object_id=visitor.pk,
                                    visited_content_type=visited_ctype,
                                    visited_object_id=visited.pk)
    

        






