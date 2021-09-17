from finance.views import (
    CreateIndexAPIView,
    GetFinanceInfoAPIView,
    ShowHistroyOfTopUpAPIView,
    TopUpBalanceAPIView,
    ShowHistroyOfСonsumptionAPIView,
)
from django.urls import path, include

urlpatterns = [
    path("get-finance-info", GetFinanceInfoAPIView.as_view()),
    path("create-index", CreateIndexAPIView.as_view()),
    path("top-up-balance", TopUpBalanceAPIView.as_view()),
    path("show-history-of-top-up", ShowHistroyOfTopUpAPIView.as_view()),
    path("show-history-of-consumption", ShowHistroyOfСonsumptionAPIView.as_view()),
]