from django.db import models

class Url_index(models.Model):
    content = models.CharField(max_length=100)
    tigger_url = models.URLField()
    ranking = models.IntegerField()
    system_ip = models.GenericIPAddressField(null=True)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Url_index'
        ordering = ['content']

    def __str__(self):
        return f"{self.content}"