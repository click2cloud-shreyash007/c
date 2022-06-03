from shop.viewsets import itemViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shop',itemViewset)

# localhost:p/api/shop/5
# GET, POST, PUT, DELETE
# list , retrive