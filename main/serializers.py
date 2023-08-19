from rest_framework import serializers
from .models import UserProfile, UserInvite


class UserProfileSerializer(serializers.ModelSerializer):
    activated_invite = serializers.CharField(max_length=6)

    class Meta:
        model = UserProfile
        fields = (
            "phone_number",
            "verification_code",
            "invite_code",
            "activated_invite",
        )


class AuthorizeUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)


class UserInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInvite
        fields = ("invite_code",)


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    verification_code = serializers.CharField(max_length=4)
