from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from occurrence_report.models import (
    OccurrenceReport,
)

class OccurrenceReportSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=OccurrenceReport.objects.all())])
    class Meta:
        model = OccurrenceReport
        fields = "__all__"
