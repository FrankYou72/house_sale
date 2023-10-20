from django.contrib import admin

from .models.item import Item
from .models.buyer import Buyer
from .models.offer import Offer

admin.site.register(Item)
admin.site.register(Buyer)
admin.site.register(Offer)