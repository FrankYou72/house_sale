from django.db import models
from rest_framework import serializers
from .buyer import Buyer, BuyerSerializer


class Payment(models.Model):
    buyer = models.ForeignKey(Buyer, models.PROTECT)
    value = models.FloatField()
    date = models.DateField(auto_now_add=True)
    voucher = models.FileField(upload_to='files/')

    class Meta:
        db_table = 'payment'
        managed = True

    def __str__(self):
        return f"{self.buyer}: R$ {self.value}"



class PaymentSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()
    class Meta:
        model = Payment
        fields = '__all__'