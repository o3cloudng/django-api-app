from email.policy import default
from django.db import models
from data_settings.models import HighestInjuryLevel, InvestigationStatus, OccurrenceCategory, OccurrenceType, State
from helpers.models import TrackingModel

class OccurrenceReport(TrackingModel, models.Model):
    title = models.CharField(max_length=200, unique=True)
    occurrence_number = models.CharField(max_length=200, blank=True)
    occurrence_category = models.ForeignKey(OccurrenceCategory, on_delete=models.CASCADE)
    occurrence_type = models.ForeignKey(OccurrenceType, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    highest_injury_level = models.ForeignKey(HighestInjuryLevel, on_delete=models.CASCADE)
    investigation_status = models.ForeignKey(InvestigationStatus, on_delete=models.CASCADE)
    event_phase = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    departure = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        permissions = [
            [
                "deactivate_occurrencereport",
                "can deactivate occurrence report",
            ],
            ["print_occurrencereport", "can print occurrence report"],
            [
                "import_occurrencereport",
                "can import occurrence report",
            ],
            [
                "export_occurrencereport",
                "can export occurrence report",
            ],
        ]

    def __str__(self):
        return self.title


class OccurenceSection(TrackingModel, models.Model):
    title = models.CharField(max_length=200, unique=True)
    occurrence_report = models.ForeignKey(OccurrenceReport, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        permissions = [
            [
                "deactivate_occurrencereport",
                "can deactivate occurrence report",
            ],
            ["print_occurrencereport", "can print occurrence report"],
            [
                "import_occurrencereport",
                "can import occurrence report",
            ],
            [
                "export_occurrencereport",
                "can export occurrence report",
            ],
        ]

    def __str__(self):
        return self.title