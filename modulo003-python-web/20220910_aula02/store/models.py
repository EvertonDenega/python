from django.db import models


class ItemsList(models.Model):

    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Publicada em")

    def __str__(self):
        return self.name


class Item(models.Model):

    item_list = models.ForeignKey(ItemsList, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)