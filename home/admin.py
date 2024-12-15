from django.contrib import admin
from .models import Job, JobApplication

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'employment_type', 'posted_by', 'date_posted')
    list_filter = ('employment_type', 'date_posted')
    ordering = ('date_posted',)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_at')

admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
