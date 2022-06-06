from django.db import models

# Create your models here.

class item(models.Model):
    item_id = models.IntegerField()

    item_name = models.CharField(max_length=100)
    
    item_price = models.CharField(max_length=10)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
