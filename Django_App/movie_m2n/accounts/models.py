from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    from_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="to_user")

    def get_score(self):
        return self.score_set.aggregate(models.Avg('value'))

    def get_recommend(self):
        return self.score_set.order_by('-value').first()
