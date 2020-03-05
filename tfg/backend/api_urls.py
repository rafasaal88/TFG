
#REST

from rest_framework import routers

from .viewsets import Product_ViewSet, Publicity_Campaign_ViewSet, User_ViewSet, Recipe_ViewSet

router = routers.SimpleRouter()

router.register('recipe_list', Recipe_ViewSet)
router.register('product_list', Product_ViewSet)
router.register('publicity_campaign_list', Publicity_Campaign_ViewSet)
router.register('user', User_ViewSet)

urlpatterns = router.urls