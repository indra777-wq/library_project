from warnings import catch_warnings

from django.contrib import admin
from django.core.cache import cache
from django.urls import path, include
from drf_yasg.app_settings import swagger_settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_views = get_schema_view(
    openapi.Info(
        title='Book list Api',
        default_version='',
        description='Library demo projects',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='indra96936@gmail.com'),
        license=openapi.License(name='demo licence'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),

    path('swagger/', schema_views.with_ui(
        'swagger', cache_timeout=0), name='swagger_swagger_ui'
         ),
    path('redoc/', schema_views.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'
         )
]
