from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('player/', views.PlayerList.as_view()),
    path('post/', views.PostList.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('replyadd/', views.ReplyAdd.as_view()),
    path('gamedata/', views.GameDataList.as_view()),
    path('player/<int:pk>', views.PlayerDetails.as_view()),
    path('post/<str:user>', views.PostDetail.as_view()),
    path('reply/<int:pk>', views.ReplyDetail.as_view()),
    path('gamedata/<int:user_id>', views.GameDataDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
