from django.db import models
from django.contrib.auth.models import User
from booktable.models import Booktable
# Create your models here.

class Managebookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Booktable, on_delete=models.CASCADE)
    # booking_cost = models.IntegerField()
    booking_confirm = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.id
    
    