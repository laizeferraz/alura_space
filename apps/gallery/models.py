from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Pictures(models.Model):
    CATEGORY_OPTIONS = [
      ("NEBULA", "Nebula"),
      ("GALAXY", "Galaxy"),
      ("STAR", "Star"),
      ("PLANET", "Planet"),
    ]
    title = models.CharField(max_length=100, null=False, blank=False)
    font = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default="")
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
      to=User, 
      on_delete=models.SET_NULL, 
      null=True, 
      blank=False,
      related_name="user"
    )
    
    def __str__(self):
        return self.title
