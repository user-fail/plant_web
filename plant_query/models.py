from django.db import models


class CommentEmoAnalysis(models.Model):
    comment = models.CharField(max_length=5000)
    emo_value = models.FloatField()
    level = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'comment_emo_analysis'


class LocationInfo(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    rank_reverse = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location_info'


class Log(models.Model):
    ip = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.CharField(max_length=10000)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=100, blank=True, null=True)
    spend_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'log'


class PlantInfo(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    rank_reverse = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plant_info'
