from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'is_aproved',
        'review',
    )

admin.site.register(Review, ReviewAdmin)