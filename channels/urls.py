from rest_framework.routers import DefaultRouter
from channels.views import MarketplaceViewSet

router = DefaultRouter()

router.register("marketplace", MarketplaceViewSet, basename="marketplace")

urlpatterns = router.urls
