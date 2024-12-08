import json
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def jsonify(value):
    """Convert a Django queryset to JSON."""
    # Check if it's a queryset, and convert it to a list of dictionaries
    if hasattr(value, 'values'):
        value = list(value.values())  # Convert QuerySet to a list of dictionaries

    # Handle datetime fields by converting them to string
    def convert_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert to ISO 8601 string format
        raise TypeError("Type not serializable")

    # Convert to JSON string
    return json.dumps(value, default=convert_datetime)
