"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
BASE_API_URL = f"https://{CODESPACE_NAME}-8000.app.github.dev/api/" if CODESPACE_NAME else "http://localhost:8000/api/"
print(f"API Base URL: {BASE_API_URL}")

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your API endpoints here, e.g.:
    # path('api/activities/', include('activities.urls')),
]
