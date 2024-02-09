from django.contrib import admin

from catalog.models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "is_done"]
    list_filter = ["is_done"]
    search_fields = ["content"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
