from django.urls import path
from . import views

app_name = 'Loan Manager'

urlpatterns = [
    path('', views.loanList.as_view(), name='loan_list'),
]
