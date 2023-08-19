import random
import string
import time
from rest_framework import status, generics
from rest_framework.response import Response
from django.db import transaction
from .models import UserProfile, UserInvite
from .serializers import (
    UserProfileSerializer,
    AuthorizeUserSerializer,
    VerifyCodeSerializer,
    UserInviteSerializer,
)


class AuthorizeUserView(generics.GenericAPIView):
    serializer_class = AuthorizeUserSerializer

    @transaction.atomic
    def post(self, request):
        serializer = AuthorizeUserSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]

            verification_code = "".join(random.choices(string.digits, k=4))
            time.sleep(random.uniform(1, 2))

            user, created = UserProfile.objects.get_or_create(phone_number=phone_number)
            if created:
                user.verification_code = verification_code
                user.generate_invite_code()
                user.save()

            return Response(
                {"message": "Verification code sent successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "phone_number"


class UsersWithInviteListView(generics.ListAPIView):
    serializer_class = AuthorizeUserSerializer

    def get_queryset(self):
        phone_number = self.kwargs["phone_number"]

        try:
            user = UserProfile.objects.get(phone_number=phone_number)
        except UserProfile.DoesNotExist:
            return UserProfile.objects.none()

        invite_code = user.activated_invite
        if invite_code:
            users = UserProfile.objects.filter(activated_invite=invite_code).exclude(
                phone_number=phone_number
            )
            return users
        return UserProfile.objects.none()


class VerifyCodeView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer

    @transaction.atomic
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            verification_code = serializer.validated_data["verification_code"]

            try:
                user = UserProfile.objects.get(phone_number=phone_number)

                if user.verification_code == verification_code:
                    user.verification_code = ""
                    user.save()
                    return Response(
                        {"message": "Verification successful"},
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"message": "Invalid verification code"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except UserProfile.DoesNotExist:
                return Response(
                    {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateInviteCodeView(generics.GenericAPIView):
    serializer_class = UserInviteSerializer

    @transaction.atomic
    def post(self, request, phone_number):
        serializer = UserInviteSerializer(data=request.data)
        if serializer.is_valid():
            invite_code = serializer.validated_data["invite_code"]

            try:
                user = UserProfile.objects.get(phone_number=phone_number)
                if not user.activated_invite:
                    if UserInvite.objects.filter(invite_code=invite_code).exists():
                        user.activated_invite = invite_code
                        user.save()
                        return Response(
                            {"message": "Invite code activated successfully"},
                            status=status.HTTP_200_OK,
                        )
                    else:
                        return Response(
                            {"message": "Invalid invite code"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                else:
                    return Response(
                        {"message": "User already has an activated invite code"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except UserProfile.DoesNotExist:
                return Response(
                    {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
