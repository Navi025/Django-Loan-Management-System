"""
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
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # matches /account/****
    path('account/', include('accounts.urls')),
    
    # matches /dashboard/****
    path('dashboard/', include('dashboard.urls')),

    # matches /asset/****
    path('asset/', include('assetmanager.urls')),

    # matches /loans/****
    path('loans/', include('loan.urls')),
]
