from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_profile_id = models.BigIntegerField(unique=True)
    display_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.display_name