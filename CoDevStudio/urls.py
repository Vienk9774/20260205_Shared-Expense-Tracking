"""
URL configuration for ExpenseTracker project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("expense/", include("ExpenseTracker.urls")),
    # Default redirect to expense list
    path("", RedirectView.as_view(url="/expense/", permanent=False)),
]
