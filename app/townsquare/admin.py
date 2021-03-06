from django.contrib import admin

from .models import Announcement, Comment, Flag, Like, Offer, OfferAction


# Register your models here.
class GenericAdmin(admin.ModelAdmin):
    list_display = ['created_on', '__str__']
    raw_id_fields = ['activity', 'profile']


class OfferActionAdmin(admin.ModelAdmin):
    list_display = ['created_on', '__str__']
    raw_id_fields = ['profile']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'key', 'valid_from', 'valid_to', '__str__']
    raw_id_fields = ['persona', 'created_by']


class AnnounceAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'valid_from', 'valid_to', '__str__']

admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferAction, OfferActionAdmin)
admin.site.register(Comment, GenericAdmin)
admin.site.register(Like, GenericAdmin)
admin.site.register(Flag, GenericAdmin)
admin.site.register(Announcement, AnnounceAdmin)
