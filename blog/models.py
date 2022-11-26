from django.db import models


class BlogProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
