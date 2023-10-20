from django.db import models
from rest_framework import serializers


class Item(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_price = models.FloatField()
    lowest_price = models.FloatField()
    bought = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        db_table = 'item'
        managed = True

    def __str__(self):
        return self.name



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'