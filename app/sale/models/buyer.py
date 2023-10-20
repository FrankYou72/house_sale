from django.db import models
from rest_framework import serializers


class Buyer(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'buyer'
        managed = True

    def __str__(self):
        return self.name



class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'