from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

from .models.item import Item
from .models.buyer import Buyer
from .models.offer import Offer


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 0



class ItemAdmin(ImportExportModelAdmin):
    def image_tag(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        except ValueError:
            return None

    list_display = ["name", "type", "start_price", "bought", "image_tag"]
    image_tag.short_description = 'Image Preview'
    inlines = [OfferInline]



class OfferAdmin(admin.ModelAdmin):
    list_display = ("buyer", "item", "value", "accepted")



class BuyerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [OfferInline]



admin.site.register(Item, ItemAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Offer, OfferAdmin)
