from operator import mod
from django.db import models

class Loss_communication(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    localization = models.TextField()
    type = models.CharField(max_length=20)
    date = models.DateField()
    events = models.ForeignKey(to='events.Events',on_delete=models.CASCADE, related_name="events")