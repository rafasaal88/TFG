
#REST

from rest_framework import routers

from .viewsets import ProductViewSet

router = routers.SimpleRouter()


router.register('product', ProductViewSet)

urlpatterns = router.urls