from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    descriptions = models.TextField(default='')

    def to_Json(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'descriptions': self.descriptions
        }


