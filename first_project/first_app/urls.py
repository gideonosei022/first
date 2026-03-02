from django.urls import path
from .views import CalculationListCreateView, CalculationDetailView

urlpatterns = [
    path('calculations/', CalculationListCreateView.as_view(), name='calculations-list-create'),
    path('calculations/<int:pk>/', CalculationDetailView.as_view(), name='calculations-detail'),
]