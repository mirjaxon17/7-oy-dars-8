from django.urls import path,include
from rest_framework import routers
from rest_framework import permissions
from .views import ShopPageView,ShopDetaiLPageView,ContactPageView,ChackOutPageView,CartPageView,TestimonialPageView,NotFoundPageView,SearchResulPageView,VegetablePageApiView,FruitPageApiView,BestSellPageApiView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        description="Music Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = routers.DefaultRouter()
router.register('fruits', FruitPageApiView)
router.register('vegetables', VegetablePageApiView)
router.register('bestsell', BestSellPageApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    path('shop/',ShopPageView.as_view(),name='shop'),
    path('shopdetail/',ShopDetaiLPageView.as_view(),name='shopdetail'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('cart/',CartPageView.as_view(),name='cart'),
    path('testimonial/',TestimonialPageView.as_view(),name='testimonial'),
    path('checkout/',ChackOutPageView.as_view(),name='checkout'),
    path('notfound/',NotFoundPageView.as_view(),name='notfound'),
    path('search/',SearchResulPageView.as_view(),name='search'),

    ]
