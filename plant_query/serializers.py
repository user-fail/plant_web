from rest_framework.serializers import ModelSerializer

from plant_query.models import PlantInfo, LocationInfo, CommentEmoAnalysis, Log


class Serializer_PlantInfo(ModelSerializer):
    class Meta:
        model = PlantInfo
        exclude = ['id']


class Serializer_LocationInfo(ModelSerializer):
    class Meta:
        model = LocationInfo
        exclude = ['id']


class Serializer_Comment_Emo_Analysis(ModelSerializer):
    class Meta:
        model = CommentEmoAnalysis
        exclude = ['id']


class Serializer_Log(ModelSerializer):
    class Meta:
        model = Log
        exclude = ['id']
