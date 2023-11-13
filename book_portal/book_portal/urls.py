"""
URL configuration for book_portal project.

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
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.conf.urls.static import static
from django.conf import settings

>>>>>>> 3bd036d (feat : Add profile model to user)
=======
from django.conf.urls.static import static
from django.conf import settings

>>>>>>> 3bd036d6c9eda4245c8140eb5533fac7964d2c31

urlpatterns = [
    path('admin/', admin.site.urls),
]
<<<<<<< HEAD
<<<<<<< HEAD
=======
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3bd036d (feat : Add profile model to user)
=======
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3bd036d6c9eda4245c8140eb5533fac7964d2c31
