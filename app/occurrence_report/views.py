from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import OccurrenceReport
from .serializers import OccurrenceReportSerializer

class OccurrenceReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = OccurrenceReport.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = OccurrenceReportSerializer

    def list(self, request):
        if not request.user.has_perm("occurence_report.view_occurencereport"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        queryset = self.get_queryset()
        serializer = OccurrenceReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.has_perm("occurence_report.add_occurrencereport"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OccurrenceReportDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  OccurrenceReport.objects.all()
    serializer_class = OccurrenceReportSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("occurence_report.view_occurrencereport"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not request.user.has_perm("occurence_report.change_occurrencereport"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.has_perm("occurence_report.delete_occurrencereport"):
            return Response({"error":"Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)

