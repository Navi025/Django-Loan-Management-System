from django.urls import path, re_path
from . import views 

app_name = 'assetmanager'
urlpatterns = [
    path('', views.assetList.as_view(), name='assetlist'),
    path('create/', views.createAsset, name='create_asset'),
    re_path(r'^update/(?P<id>\d+)/$', views.asset_update, name="update_asset"),
    re_path(r'^delete/(?P<id>\d+)/$', views.asset_delete, name="delete_asset"),
]
