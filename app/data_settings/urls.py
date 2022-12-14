from django.urls import path
from data_settings.views import (
    OccurrenceTypeListCreateAPIView,
    OccurrenceTypeDetailAPIView,
    InvestigationStatusListCreateAPIView,
    InvestigationStatusDetailAPIView,
    OccurrenceCategoryListCreateAPIView,
    OccurrenceCategoryDetailAPIView,
    ReportStatusListCreateAPIView,
    ReportStatusDetailAPIView,
    HighestInjuryLevelListCreateAPIView,
    HighestInjuryLevelDetailAPIView,
    DamageToAirCraftAPIView,
    DamageToAirCraftDetailsAPIView,
    StateListCreateAPIView,
    StateDetailAPIView,
    APIProviderListCreateAPIView,
    APIProviderDetailAPIView,
    CountryListCreateAPIView,
    CountryDetailAPIView,
    CityListCreateAPIView,
    CityDetailAPIView,
    AirportListCreateAPIView,
    AirportDetailAPIView,
    AirplaneListCreateAPIView,
    AirplaneDetailAPIView,
    AirportDetailAPIView,
    ManufacturerListCreateAPIView,
    ManufacturerDetailAPIView,
    aircraft_manufacturer_import,
)

urlpatterns = [
    path(
        "occurrencetype/",
        OccurrenceTypeListCreateAPIView.as_view(),
        name="occurrence-type",
    ),
    path(
        "occurrencetype/<int:id>/",
        OccurrenceTypeDetailAPIView.as_view(),
        name="occurrence-type-details",
    ),
    path(
        "investigationstatus/",
        InvestigationStatusListCreateAPIView.as_view(),
        name="investigation-status",
    ),
    path(
        "investigationstatus/<int:id>/",
        InvestigationStatusDetailAPIView.as_view(),
        name="investigation-status-details",
    ),
    path(
        "occurrencecategory/",
        OccurrenceCategoryListCreateAPIView.as_view(),
        name="occurrencecategory",
    ),
    path(
        "occurrencecategory/<int:id>/",
        OccurrenceCategoryDetailAPIView.as_view(),
        name="occurrencecategory-details",
    ),
    path("reportstatus/", ReportStatusListCreateAPIView.as_view(), name="reportstatus"),
    path(
        "reportstatus/<int:id>/",
        ReportStatusDetailAPIView.as_view(),
        name="reportstatus-details",
    ),
    path("state/", StateListCreateAPIView.as_view(), name="state"),
    path("state/<int:id>/", StateDetailAPIView.as_view(), name="state-details"),
    path(
        "highestinjurylevel/",
        HighestInjuryLevelListCreateAPIView.as_view(),
        name="highestinjurylevel",
    ),
    path(
        "highestinjurylevel/<int:id>/",
        HighestInjuryLevelDetailAPIView.as_view(),
        name="highestinjurylevel-details",
    ),
    path(
        "damages_to_aircraft/",
        DamageToAirCraftAPIView.as_view(),
        name="damages_to_aircraft",
    ),
    path(
        "damages_to_aircraft/<int:id>/",
        DamageToAirCraftDetailsAPIView.as_view(),
        name="damages_to_aircraft-details",
    ),
    path(
        "api_provider/",
        APIProviderListCreateAPIView.as_view(),
        name="api_provider",
    ),
    path(
        "api_provider/<int:id>/",
        APIProviderDetailAPIView.as_view(),
        name="api-provider-details",
    ),
    path(
        "country/",
        CountryListCreateAPIView.as_view(),
        name="country",
    ),
    path(
        "country/<int:id>/",
        CountryDetailAPIView.as_view(),
        name="country-detail",
    ),
    path(
        "city/",
        CityListCreateAPIView.as_view(),
        name="city",
    ),
    path(
        "city/<int:id>/",
        CityDetailAPIView.as_view(),
        name="city-detail",
    ),
    path(
        "airport/",
        AirportListCreateAPIView.as_view(),
        name="airport",
    ),
    path(
        "airport/<int:id>/",
        AirportDetailAPIView.as_view(),
        name="airport-detail",
    ),
    path(
        "airline/",
        AirplaneListCreateAPIView.as_view(),
        name="airline",
    ),
    path(
        "airline/<int:id>/",
        AirplaneDetailAPIView.as_view(),
        name="airline-detail",
    ),
    path(
        "manufacturer/",
        ManufacturerListCreateAPIView.as_view(),
        name="manufacturer",
    ),
    path(
        "manufacturer/<int:id>/",
        ManufacturerDetailAPIView.as_view(),
        name="manufacturer-detail",
    ),
    path(
        "manufacturer/import/",
        aircraft_manufacturer_import,
        name="import_aircraft_template_data_api",
    ),
]
