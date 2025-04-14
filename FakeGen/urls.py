from django.contrib import admin
from django.urls import path
from user.views import UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', UserList.as_view()),
]
