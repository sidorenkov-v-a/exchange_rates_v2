from django.urls import include, path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, test

router = DefaultRouter()
router.register('currency', CurrencyViewSet)

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
    path('test/<int:add_time>', test),
    path('', include(router.urls)),
    path('', RedirectView.as_view(pattern_name='currency-list')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='API проекта Exchange rates',
        default_version='v1',
        description='Проект выполнен в рамках тестового задания',
        contact=openapi.Contact(
            name='Владислав',
            email='sidorenkov.v.a@yandex.ru',
            url='https://github.com/sidorenkov-v-a',
            telegram='https://t.me/sidorenkov_vl'
        ),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
