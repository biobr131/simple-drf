from django.urls import path

from accounts.views import UserListView, UserDetailView

app_name = "accounts"
urlpatterns = [
    path("api/users", UserListView.as_view(), name="user_list"),
    path("api/user/<str:username>", UserDetailView.as_view(), name="user_detail"),
]
