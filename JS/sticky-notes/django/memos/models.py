from django.db import models


class Memo(models.Model):
    content = models.TextField()
