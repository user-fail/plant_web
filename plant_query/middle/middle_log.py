import time

from ..serializers import Serializer_Log
from ..util.get_request_info import extract_request_info


def log_middleware(get_response):
    def middlewares(request):
        # 记录user基本信息
        start_time = time.time()

        # 获取响应
        response = get_response(request)

        # 花费时间
        spend_time = int((time.time() - start_time) * 1000)

        # 获取请求信息
        data = extract_request_info(request)
        data.update({'spend_time': spend_time})

        # 序列化并储存
        serializer = Serializer_Log(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return response

    return middlewares
