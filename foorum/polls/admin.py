from django.contrib import admin
from . import models
#from .models import Comment, Question

# Register your models here.
admin.site.register(models.Question)
admin.site.register(models.Response)

#admin.site.register(models.Comment)
#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'body', 'post', 'created_on', 'active')
#    list_filter = ('active', 'created_on')
#    search_fields = ('name', 'email', 'body')
#    actions = ['approve_comments']
#
#    def approve_comments(self, request, queryset):
#        queryset.update(active=True)

# Register your models here