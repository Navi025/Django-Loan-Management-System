from django.urls import path, re_path
from . import views 
from .views import HomeView

app_name = 'dashboard'
urlpatterns = [
    # /dashboard/
    path('', HomeView.as_view(), name='home'),
    path('loan_type/', views.loantype, name='loanType'),
    path('product/create/', views.product_create, name='create_product'),
    re_path(r'^product/update/(?P<id>\d+)/$', views.product_update, name="update_product"),
    re_path(r'^product/delete/(?P<id>\d+)/$', views.product_delete, name="delete_product"),
]















