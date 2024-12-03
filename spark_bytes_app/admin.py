from django.contrib import admin
from .models import Profile, Event

admin.site.register(Profile)
admin.site.register(Event)

# class EventAdmin(admin.ModelAdmin):
#    list_display = ('name', 'location', 'date', 'created_by', 'current_reservations', 'reservation_limit')
#    list_filter = ('location', 'date')  # Add filters for location and date
#    search_fields = ('name', 'created_by__user__username')  # Add search functionality
#    list_editable = ('reservation_limit',)  # Allow inline editing of the reservation limit

#    def current_reservations(self, obj):
#        return obj.reserved_by.count()
#    current_reservations.short_description = 'Current Reservations'

# admin.site.register(Event, EventAdmin)
