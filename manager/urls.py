from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('accounts',views.Accounts, basename='all_accounts')
router.register('assets_liabilities', views.AssetLiability, basename='all_assests_and_liabilities')

urlpatterns = [
    path('',include(router.urls)),
    path('categories/', views.CategoriesListCreateView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoriesRetrieveDestroyAPIView.as_view(), name='category_detail'),
    path('transactions/', views.TransactionListCreateView.as_view(), name = 'transaction_list'),
    path('transactions/<int:pk>/', views.TransactionsRetrieveDestroyAPIView.as_view(), name = 'transaction_detail')
]