from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('book', BookViewSet)
router.register('shop', ShopViewSet)
router.register('book-sold', BookSoldViewSet)
router.register('in-stock', InStockViewSet)
router.register('purchase', PurchaseViewSet)
router.register('seller', SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('book-year/<int:year_published>/', BooksByPublicationYearView.as_view()),
    path('book-recently-year/', BooksRecentlyPublishedView.as_view()),
]