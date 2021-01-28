from rest_framework.serializers import ModelSerializer

from tourism.models import Field_of_activity, Toursites


class FieldOfActivSerializer(ModelSerializer):
    class Meta:
        model = Field_of_activity
        fields = ["name"]

class ToursitesSerializer(ModelSerializer):
    field_of_activity = FieldOfActivSerializer()

    class Meta:
        model = Toursites
        fields = "__all__"
