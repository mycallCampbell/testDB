

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.

class Rolex(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    goLive = models.CharField(max_length=200, null=True, blank=True)
    nickName = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    titleBackend = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    ref = models.CharField(max_length=200, null=True, blank=True)
    strap = models.CharField(max_length=200, null=True, blank=True)
    dial = models.CharField(max_length=200, null=True, blank=True)
    imageAmount = models.CharField(max_length=200, null=True, blank=True)
    strapMaterial = models.CharField(max_length=200, null=True, blank=True)
    strapColour = models.CharField(max_length=200, null=True, blank=True)
    strapClasp = models.CharField(max_length=200, null=True, blank=True)
    dialSize = models.CharField(max_length=200, null=True, blank=True)
    numberMarkers = models.CharField(max_length=200, null=True, blank=True)
    hands = models.CharField(max_length=200, null=True, blank=True)
    caseMaterial = models.CharField(max_length=200, null=True, blank=True)
    bezel = models.CharField(max_length=200, null=True, blank=True)
    bezelStyle = models.CharField(max_length=200, null=True, blank=True)
    bezelDirection = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    caliber = models.CharField(max_length=200, null=True, blank=True)
    movement = models.CharField(max_length=200, null=True, blank=True)
    powerReserve = models.CharField(max_length=200, null=True, blank=True)
    waterResistant = models.CharField(max_length=200, null=True, blank=True)
    numberOfJewels = models.CharField(max_length=200, null=True, blank=True)
    crystal = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    box = models.CharField(max_length=200, null=True, blank=True)
    card = models.CharField(max_length=200, null=True, blank=True)
    condition = models.CharField(max_length=200, null=True, blank=True)
    warranty = models.CharField(max_length=200, null=True, blank=True)
    availble = models.CharField(max_length=200, null=True, blank=True)
    descriptionMobile = models.TextField(null=True, blank=True)
    descriptionDesktop = models.TextField(null=True, blank=True)
    descriptionSmall = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.titleBackend)

