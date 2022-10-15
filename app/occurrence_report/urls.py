from django.urls import path
from occurrence_report.views import (
    OccurrenceReportDetailAPIView,
    OccurrenceReportListCreateAPIView,
)

urlpatterns = [
    path(
        "",
        OccurrenceReportListCreateAPIView.as_view(),
        name="occurrence-report",
    ),
    path(
        "<int:id>/",
        OccurrenceReportDetailAPIView.as_view(),
        name="occurrence-report-details",
    ),
]
