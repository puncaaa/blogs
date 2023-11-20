from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, BlogPostViewSet, CommentViewSet, LikeViewSet, SubscriptionViewSet, \
    UserRegistrationView, UserLoginView, UserRegisterViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'blogposts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/create/', UserRegisterViewSet.as_view(), name='create'),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
]
