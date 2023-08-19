from django.db import models
import random
import string


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=4, blank=True)
    invite_code = models.CharField(max_length=6, blank=True)
    activated_invite = models.CharField(max_length=6, blank=True)

    def generate_invite_code(self):
        if not self.invite_code:
            self.invite_code = "".join(
                random.choices(string.digits + string.ascii_letters, k=6)
            )
            self.save()

    def __str__(self):
        return self.phone_number


class UserInvite(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name="invites", on_delete=models.CASCADE
    )
    invite_code = models.CharField(max_length=6)
