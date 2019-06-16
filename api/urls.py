from rest_framework import routers

from api import viewsets

router = routers.SimpleRouter()
router.register(r'posts', viewsets.PostViewSet)

urlpatterns = router.urls
