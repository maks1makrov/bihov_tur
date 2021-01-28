from rest_framework.serializers import ModelSerializer

from tourism.models import Field_of_activity, Toursites, Articles


class FieldOfActivSerializer(ModelSerializer):
    class Meta:
        model = Field_of_activity
        fields = "__all__"

class ToursitesSerializer(ModelSerializer):
    field_of_activity = FieldOfActivSerializer(many=True)

    class Meta:
        model = Toursites
        fields = "__all__"


class ArticlesSerializer(ModelSerializer):
    toursite_id = ToursitesSerializer(many=True)

    class Meta:
        model = Articles
        fields = "__all__"