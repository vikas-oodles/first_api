from rest_framework import routers
from myapp.viewsets import ProfileViewsets, UserViewsets

router = routers.DefaultRouter()
router.register('profile',ProfileViewsets)
router.register('user',UserViewsets)
