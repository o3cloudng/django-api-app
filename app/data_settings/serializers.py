from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from data_settings.models import (
    Manufacturer,
    OccurrenceType,
    InvestigationStatus,
    OccurrenceCategory,
    ReportStatus,
    State,
    HighestInjuryLevel,
    DamageToAirCraft,
    APIProvider,
    Country,
    City,
    Airport,
    Airplane,
)


class OccurrenceTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=OccurrenceType.objects.all())])
    class Meta:
        model = OccurrenceType
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class InvestigationStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=InvestigationStatus.objects.all())])
    class Meta:
        model = InvestigationStatus
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class OccurrenceCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=OccurrenceCategory.objects.all())])
    class Meta:
        model = OccurrenceCategory
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class ReportStatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=ReportStatus.objects.all())])
    class Meta:
        model = ReportStatus
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class StateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=State.objects.all())])
    class Meta:
        model = State
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class HighestInjuryLevelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=HighestInjuryLevel.objects.all())])
    class Meta:
        model = HighestInjuryLevel
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class DamageToAirCraftSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=DamageToAirCraft.objects.all())])
    class Meta:
        model = DamageToAirCraft
        fields = "__all__"


class APIProviderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=APIProvider.objects.all())])
    access_key = serializers.CharField(max_length=68)
    class Meta:
        model = APIProvider
        fields = [
            "id",
            "name",
            "endpoint",
            "access_key"
        ]


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Country.objects.all())])
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=City.objects.all())])
    class Meta:
        model = City
        fields = "__all__"


class AirportSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Airport.objects.all())])
    class Meta:
        model = Airport
        fields = "__all__"


class AirplaneSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Airplane.objects.all())])
    class Meta:
        model = Airplane
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Manufacturer.objects.all())])
    class Meta:
        model = Manufacturer
        fields = "__all__"
