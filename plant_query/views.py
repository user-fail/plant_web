import random

from django.db.models.functions import Random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PlantInfo, LocationInfo, CommentEmoAnalysis
from .serializers import Serializer_LocationInfo, Serializer_PlantInfo, Serializer_Comment_Emo_Analysis


# 获取工厂数据
@api_view(['get'])
def get_plant_data(request):
    params = request.query_params
    page = int(params['page']) * 10
    size = 10
    # 判断size是否存在
    if params.get('size'):
        size = int(params['size'])
    if size > 50:
        return Response({'code': 200, "message": '错误请求'}, status.HTTP_404_NOT_FOUND)
    if size > page:
        page = size
    total = PlantInfo.objects.count()
    query_result = PlantInfo.objects.filter(id__range=(page - size, page))
    serializer = Serializer_PlantInfo(instance=query_result, many=True).data
    return Response({'code': 200, "data": {'total': total, "result": serializer}}, status.HTTP_200_OK)


# 获取位置信息
@api_view(['get'])
def get_location_data(request):
    params = request.query_params
    page = int(params['page']) * 10
    size = 10
    # 判断size是否存在
    if params.get('size'):
        size = int(params['size'])
    if size > 50:
        return Response({'code': 200, "message": '错误请求'}, status.HTTP_404_NOT_FOUND)
    if size > page:
        page = size
    total = LocationInfo.objects.count()
    query_result = LocationInfo.objects.filter(id__range=(page - size, page))
    serializer = Serializer_LocationInfo(instance=query_result, many=True).data
    return Response({'code': 200, "data": {'total': total, "result": serializer}}, status.HTTP_200_OK)


# random comment
@api_view(['get'])
def random_comment(request):
    num_comments = random.randint(100, 200)
    comments = CommentEmoAnalysis.objects.order_by(Random())[:num_comments]
    serialize = Serializer_Comment_Emo_Analysis(instance=comments, many=True)
    return Response({'code': 200, "data": serialize.data}, status.HTTP_200_OK)


# 获取评论信息
@api_view(['get'])
def get_comment_analysis(request):
    page = int(request.query_params['page']) - 1
    range_start = page * 50
    total = CommentEmoAnalysis.objects.count()
    data = CommentEmoAnalysis.objects.filter(id__range=(range_start, range_start + 50))
    serializer = Serializer_Comment_Emo_Analysis(instance=data, many=True)
    return Response({'code': 200, 'data': {
        'total': total,
        "comments": serializer.data
    }}, status.HTTP_200_OK)
