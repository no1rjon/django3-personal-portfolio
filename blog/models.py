from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title