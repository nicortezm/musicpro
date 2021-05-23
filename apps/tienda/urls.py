from django.urls import path,include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',views.ProductViewset)

urlpatterns = [
    path('',views.store, name='store'),
    path('categoria/<slug:category_slug>/',views.store, name='products_by_category'),
    path('categoria/<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),
    path('buscar/',views.search, name='search'),
    path('api/', include(router.urls)),
]

