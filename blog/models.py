from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title