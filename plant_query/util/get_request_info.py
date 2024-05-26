def extract_request_info(request) -> dict:
    """
    :param request: HttpRequest实例
    :return: dict
    """
    request_method = request.method
    request_url = request.path
    ip = request.META.get('HTTP_X_REAL_IP')
    ua = request.headers['User-Agent']
    return {"method": request_method, 'url': request_url, "ip": ip, "user_agent": ua}