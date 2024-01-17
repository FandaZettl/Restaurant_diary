from django.urls import path
from .views import VisitListCreateView, VisitDetailView

urlpatterns = [
    path('visits/', VisitListCreateView.as_view(), name='visit-list-create'),
    path('visits/<int:pk>/', VisitDetailView.as_view(), name='visit-detail')
]
