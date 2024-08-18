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
