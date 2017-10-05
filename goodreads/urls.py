"""goodreads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/authors/', include('modules.Authors.urls')),
    url(r'^api/v1/books/', include('modules.Books.urls', namespace='books')),
    url(r'^api/v1/users/', include('modules.Users.urls')),
    url(r'^api/v1/auth/$', obtain_jwt_token),
    url(r'^api/v1/auth/refresh/$', refresh_jwt_token),
    url(r'^api/v1/auth/verify/$', verify_jwt_token),
    url(r'^docs/', include_docs_urls(title="Goodreads API")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)