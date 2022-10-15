from urllib import request

import jwt
from data_settings.models import *
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import filters, generics, permissions, status
from rest_framework.generics import (  # RetrieveUpdateAPIView, DestroyAPIView  #CreateAPIView, ListAPIView,
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import serializers
from accounts.methods import assign_group_permissions
from accounts.pagination import CustomPageNumberPagination

from .models import User
from .serializers import AddUserRoleSerializer  # UserRoleSerializer,
from .serializers import (ChangePasswordSerializer, ContentTypeSerializer,
                          LogoutSerializer, PasswordResetSerializer,
                          ReactivateSerializer, RegisterSerializer,
                          RoleSerializer, UserUpdateSerializer, )
from .utils import Util


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        default_error_message = {
            "error": "No active account found with the given credentials."
        }

        # Add custom claims
        token["email"] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# User Creation and List of all Active Users
class RegisterListAPIView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "type",
        "username",
        "password",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "type",
        "username",
    ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

            user_data = serializer.data

            user = User.objects.get(email=user_data["email"])

            token = RefreshToken.for_user(user).access_token

            # print("MY ERRORS ARE HERE")
            # current_site = get_current_site(request).domain
            current_site = self.request.environ["HTTP_HOST"]

            relativeLink = reverse("email-verify")
            absurl = current_site + relativeLink + "?token=" + str(token)

            email_body = (
                "Hi "
                + user.first_name
                + ",\n\nYou have been registered on ARGUE platform. \n\n To complete your registration, use the link below to confirm this email belongs to you \n\n"
                + "http://"
                + absurl
                # + "/api/user/verify-otp-email/"
            )
            data = {
                "email_body": email_body,
                "to_email": user.email,
                "email_subject": "ARGUE: Verify Your Email",
            }
            Util.send_email(data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error(), status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return User.objects.filter(is_deleted=False)


#  Verify Email
class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get("token")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response(
                {"message": "Successfully activated"}, status=status.HTTP_200_OK
            )

        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST
            )


# Read, Update & Delete Users
class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("accounts.view_user"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not request.user.has_perm("accounts.change_user"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=kwargs['id'])
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm("accounts.delete_user"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)


# RAECTIVATD USER
class ReactivateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ReactivateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# User Creation and List of all Users including deactivated users
class AllUsersListAPIView(ListAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "username",
        "password",
        "is_deleted",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "username",
        "password",
    ]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return User.objects.all()


class PasswordResetAPIView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        # print("#### EMAIL #####")
        # print(request.data.email)

        # otp = "123456"

        user = User.objects.get(email=user_data["email"])

        if not user:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)

        current_site = self.request.environ["HTTP_HOST"]

        email_body = (
            "Hi "
            + user.username
            + "\n\n, Use the OTP below to reset your password\n\n"
            + otp
            + "\n\n"
            + "http://"
            + current_site
            + "/api/user/verify-otp-email/"
        )
        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "ARGUE: Password Reset",
        }

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class ConfirmPasswordResetAPIView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def put(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        otp = "123456"

        user = User.objects.get(email=user_data["email"])

        current_site = self.request.environ["HTTP_HOST"]

        email_body = (
            "Hi "
            + user.username
            + "\n\n, Use the OTP below to reset your password\n\n"
            + otp
            + "\n\n"
            + "http://"
            + current_site
            + "/api/user/verify-otp-email/"
        )
        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "ARGUE: Password Reset",
        }

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class ChangePasswordAPIView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            "User Logged out successfully", status=status.HTTP_204_NO_CONTENT
        )


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):

    email_plaintext_message = "{}?token={}".format(
        reverse("password_reset:reset-password-request"), reset_password_token.key
    )

    send_mail(
        # title:
        "Password Reset for {title}".format(title="ARGUE"),
        # message:
        email_plaintext_message,
        # from:
        "olumideo@synercomgroup.net",
        # to:
        [reset_password_token.user.email],
    )

class ProfileDetailsAPIView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        pk = request.user.id
        user = User.objects.get(id=pk)
        serializer = serializers.ProfileSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #####  ROLES
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        if not request.user.has_perm("auth.view_group"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = self.get_queryset()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.add_group"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.view_group"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if self.request.data["name"] == "":
            return Response({"error":"Role not found."}, status=status.HTTP_404_NOT_FOUND)
        # if not id:
        #     return Response({"error":"Not found."}, status=status.HTTP_404_NOT_FOUND)
        if not request.user.has_perm("auth.change_group"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.delete_group"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)


#### Add User To Role
class AddUserRoleAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddUserRoleSerializer
    queryset = Group.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "No action here"}, status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request, *args, **kwargs):
        if (str(request.data["user"]) == "") | (str(request.data["role"]) == ""):
            # print(str(request.data["user"]))
            return Response({"error": "Select role and user.", "status_code": 400})

        role = Group.objects.get(pk=request.data["role"])
        user = User.objects.get(pk=request.data["user"])

        urole = []
        print(user)
        for i in user.groups.all():
            urole.append(i.name)

        add_role = role.user_set.add(user)
        user = str(user)
        if add_role == False:
            return Response(
                ({"error": "Role assignment to user failed.", "status_code": "200"})
            )

        return Response(
            {
                "user": user,
                "roles": urole,
                "message": "Role assigned to user successfully",
                "status_code": 201,
            }
        )

    def delete(self, request, *args, **kwargs):
        if (str(request.data["user"]) == "") | (str(request.data["role"]) == ""):
            return Response({"error": "Select role and user.", "status_code": 400})

        role = Group.objects.get(pk=request.data["role"])
        user = User.objects.get(pk=request.data["user"])

        urole = []
        for i in user.groups.all():
            urole.append(i.name)

        if (role != "") & (user != ""):
            role.user_set.remove(user)

            user = str(user)
            return Response(
                {
                    "user": user,
                    "roles": urole,
                    "message": "User removed from role successfully",
                    "status_code": 204,
                }
            )

        else:
            return Response({"error": "User or role not found.", "status_code": 200})

        # import pdb
        # pdb.set_trace()
        # print(user)

        # return Response(role, user)


#### Permissions
class PermissionAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # print(request.data)
        # role = Group.objects.get(name=role_name)
        # print(role)
        # if not role:
        #     return Response({"error": "Role not selected."})

        # print(role)
        role_name = request.data["role_name"]
        print(role_name)
        role_permissions = Group.objects.get(name=role_name).permissions.all().values()
        # role_perm = serializers.serializer("json", role_permissions)

        return Response(list(role_permissions))

    def post(self, request, *args, **kwargs):
        role = Group.objects.get(name=request.data["role_name"])
        if not role:
            return Response({"error": "Role not selected."})

        # Data Settings Permission
        if not request.data["module"]:
            return Response({"error": "Module not selected."})

        # print("#### MODULE")
        # print(request.data["module"])

        module = eval(request.data["module"])
        ct = ContentType.objects.get_for_model(module)
        
        if str(request.data["can_view"]) == "False":
            code_name = "view_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "view_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)
            

        if str(request.data["can_add"]) == "False":
            code_name = "add_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "add_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)


        if str(request.data["can_edit"]) == "False":
            code_name = "change_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "change_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)


        if str(request.data["can_delete"]) == "False":
            code_name = "delete_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "delete_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)


        if str(request.data["can_import"]) == "False":
            code_name = "import_"+ request.data["module"].str.lower()
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "import_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)


        if str(request.data["can_export"]) == "False":
            code_name = "export_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "export_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)


        if str(request.data["can_deactivate"]) == "False":
            code_name = "deactivate_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "deactivate_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)

        if str(request.data["can_print"]) == "False":
            code_name = "print_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.remove(permission)
        else:
            code_name = "print_"+ str.lower(request.data["module"])
            permission = Permission.objects.get(
                codename=code_name, content_type=ct
                )
            role.permissions.add(permission)
            
        role_name = request.data["role_name"]
        print(role_name)
        role_permissions = Group.objects.get(name=role_name).permissions.all().values()
        
        return Response({
            "message": "Permissions assigned to role successfully.",
            "permissions":request.data 
            })

