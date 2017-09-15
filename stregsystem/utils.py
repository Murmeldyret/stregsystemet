import datetime
from django.db.models import Q, F


def make_active_productlist_query():
    now = datetime.datetime.now()
    return (
        Q(active=True)
        & (Q(deactivate_date=None) | Q(deactivate_date__gte=now))
        & (Q(quantity=None) | Q(quantity__gt=F("bought")))
    )