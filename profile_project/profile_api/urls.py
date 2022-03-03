
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profile_api import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewSet')
router.register('profile',views.UserProfileViewset,)
router.register('feed',views.UserProfileFeedViewSet,)

urlpatterns = [
  
    path('hello-view',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
