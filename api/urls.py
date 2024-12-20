from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContactViewSet, UserSearchView, ContactSearchView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/users/', UserSearchView.as_view(), name='user_search'),
    path('search/contacts/', ContactSearchView.as_view(), name='contact_search'),
    path('', include(router.urls)),
]
