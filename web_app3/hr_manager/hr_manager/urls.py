"""
URL configuration for hr_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from catalog.views import ProductViewSet
from hr.views import HomePage_view
from hr.views import contact_view
from hr.views import employer_view
from hr.views import upload_view
from hr.views import register_view
from hr.views import send_email_view
from hr.views import RegisterViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet, "register")  # daca vrem prin API
router.register(r'products', ProductViewSet, "products")
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', HomePage_view, name="home"),
    path('contact/', contact_view, name='contact'),
    path('employers/', employer_view, name='employer'),
    path('upload/', upload_view, name='upload'),
    path('send_email/', send_email_view, name='send_email'),
    path('register/', register_view, name='register'),

    path('api/', include(router.urls)),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name='auth'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='auth_refresh'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# HTTP 200 OK
# Allow: POST, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjgzNTI1OCwiaWF0IjoxNzAyNzQ4ODU4LCJqdGkiOiJhZjE2YWVjNGI5NzA0NmM2YWFmMDE2MmY2OGQyMDI3NSIsInVzZXJfaWQiOjJ9.Sy9TGR9FPI9iXpP0P38HMPp8P8gAOiYeE2Syz_KiB3c",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNzQ5MTU4LCJpYXQiOjE3MDI3NDg4NTgsImp0aSI6ImQxYzRjODQxMmM0OTQ3MTQ4NzU4Y2QxM2RjOGExZDM3IiwidXNlcl9pZCI6Mn0.E-m7CbJIWNt-VSQCeUAIMkC9-0LRSfY2DjAQ2ybXg7c"
# }
