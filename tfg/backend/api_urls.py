
#REST

from rest_framework import routers

from .viewsets import ProductViewSet, Publicity_Campaign_ViewSet, User_ViewSet, Product_Serializer_New_ViewSet

router = routers.SimpleRouter()


router.register('product_list', ProductViewSet)
router.register('publicity_campaign_list', Product_Serializer_New_ViewSet)
router.register('user', User_ViewSet)

urlpatterns = router.urls