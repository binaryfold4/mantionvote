from django.contrib import admin
from .models import Track, Vote

class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'modified_at']

class VoteAdmin(admin.ModelAdmin):
    list_display = ['track', 'user', 'voteset_current', 'created_at']
    list_filter = ['voteset_current', 'user']

admin.site.register(Track, TrackAdmin)
admin.site.register(Vote, VoteAdmin)

