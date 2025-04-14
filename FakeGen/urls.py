from django.contrib import admin
from django.urls import path

from article.models import Article
from article.views import ArticleList
from company.views import CompanyList
from user.views import UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', UserList.as_view()),
    path('api/company', CompanyList.as_view()),
    path('api/article', ArticleList.as_view()),
]
