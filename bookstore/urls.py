from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    re_path('bookstore/', include('order.urls')),
    re_path('bookstore/', include('product.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
