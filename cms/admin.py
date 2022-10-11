from django.contrib import admin

from cms.models import Page,ContentVideo,ContentText,ContentAudio

class ContentVideoInline(admin.TabularInline):
    model = ContentVideo
    search_fields = ['title', ]

class ContentTextInline(admin.TabularInline):
    model = ContentText

class ContentAudioInline(admin.TabularInline):
    model = ContentAudio

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
   inlines = [ContentVideoInline,ContentTextInline, ContentAudioInline]
   search_fields = ['title',]

@admin.register(ContentVideo)
class ContentVideoAdmin(admin.ModelAdmin):
   search_fields = ['title',]

@admin.register(ContentText)
class ContentTextAdmin(admin.ModelAdmin):
   search_fields = ['title',]

@admin.register(ContentAudio)
class ContentAudioAdmin(admin.ModelAdmin):
   search_fields = ['title', ]

