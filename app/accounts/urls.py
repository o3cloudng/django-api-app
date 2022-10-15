from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import (  # DeactivatedUserDetailAPIView,; UserRoleCreateAPIView,; UserRoleDetailAPIView,
    AddUserRoleAPIView, AllUsersListAPIView, ChangePasswordAPIView,
    ConfirmPasswordResetAPIView, LogoutAPIView, MyTokenObtainPairView,
    PasswordResetAPIView, PermissionAPIView, ProfileDetailsAPIView,
    ReactivateAPIView, RegisterListAPIView, RoleDetailAPIView,
    RoleListCreateAPIView, UserDetailAPIView, VerifyEmail)


urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("allusers/", AllUsersListAPIView.as_view(), name="all-users"),
    # path(
    #     "deactivated-users/"
    #     DeactivatedUserDetailAPIView.as_view(),
    #     name="deactivated-user-list",
    # ),
    path("", RegisterListAPIView.as_view(), name="register"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="users"),
    path(
        "reactivate-user/<int:id>/",
        ReactivateAPIView.as_view(),
        name="reactivate-user",
    ),
    # path('delete/<int:id>', UserSoftDelete, name="delete"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path(
        "password-reset-otp/",
        PasswordResetAPIView.as_view(),
        name="password-reset-otp",
    ),
    path(
        "user/confirm-password-reset-otp/",
        ConfirmPasswordResetAPIView.as_view(),
        name="confirm-password-reset-otp",
    ),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("role/", RoleListCreateAPIView.as_view(), name="role-list-create"),
    path("role/<int:id>/", RoleDetailAPIView.as_view(), name="role-detail"),
    path(
        "add_roles_permissions/",
        PermissionAPIView.as_view(),
        name="add_roles_permission",
    ),
    # path("permissions/", PermissionAPIView.as_view(), name="permission-detail"),
    # path(
    #     "permissions/<int:id>/",
    #     PermissionDetailAPIView.as_view(),
    #     name="permission-detail",
    # ),
    path("add_user_role/", AddUserRoleAPIView.as_view(), name="add-user-role"),
    # path('role/', RoleListCreateAPIView.as_view(), name='role'),
    # path('role/<int:id>/', RoleDetailAPIView.as_view(), name='role-detail'),
    # path('user_role/', UserRoleCreateAPIView.as_view(), name='user-role'),
    # path('user_role/<int:id>/', UserRoleDetailAPIView.as_view(), name='user-role-detail'),
    path("profile/", ProfileDetailsAPIView.as_view(), name="profile"),
    path("profile/<int:id>", ProfileDetailsAPIView.as_view(), name="profile-edit"),
]
