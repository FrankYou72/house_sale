from django.db import models
from rest_framework import serializers
from .item import Item, ItemSerializer
from .buyer import Buyer, BuyerSerializer


class Offer(models.Model):
    buyer = models.ForeignKey(Buyer, models.PROTECT)
    item = models.ForeignKey(Item, models.PROTECT)
    value = models.FloatField()
    accepted = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'offer'
        managed = True

    def __str__(self):
        return f"{self.buyer} ==> {self.item} : R$ {self.value}"



class OfferSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    buyer = BuyerSerializer()
    class Meta:
        model = Offer
        fields = '__all__'