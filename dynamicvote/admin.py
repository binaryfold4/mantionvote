from django.contrib import admin
#from import_export import resources, fields
#from import_export.admin import ImportExportActionModelAdmin
from .models import Track, VoteSet

#class TrackResource(resources.ModelResource):
#    class Meta:
#        model = Track
#        skip_unchanged = True
#        report_skipped = True
#        uploaded_at = fields.Field(column_name='created_at')

class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'created_at']

admin.site.register(Track, TrackAdmin)
admin.site.register(VoteSet)

