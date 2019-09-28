from django.db import models

class SearchSource(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=2000)
    support_https = models.BooleanField(default=True)
    
