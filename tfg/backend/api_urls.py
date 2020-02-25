
#REST

from rest_framework import routers

from .viewsets import ProductViewSet, Publicity_Campaign_ViewSet

router = routers.SimpleRouter()


router.register('product_list', ProductViewSet)
router.register('publicity_campaign_list', Publicity_Campaign_ViewSet)

urlpatterns = router.urls