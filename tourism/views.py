from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views import View

from tourism.models import Field_of_activity, Toursites
from tourism.serializer import FieldOfActivSerializer, ToursitesSerializer


class ListFieldAPI(ListAPIView):
    serializer_class = FieldOfActivSerializer

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Field_of_activity.objects.filter(id=self.kwargs.get('id'))
        return Field_of_activity.objects.all()

class ListToursitesAPI(ListAPIView):
    serializer_class = ToursitesSerializer

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Toursites.objects.filter(id=self.kwargs.get('id'))
        return Toursites.objects.all()

class TestIndex(View):
    def get(self, request):
        response = {}
        response['content'] = Toursites.objects.prefetch_related('field_of_activity').all()
        return render(request, 'index.html', response)