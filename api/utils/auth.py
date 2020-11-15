from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from api import models
from django_redis import get_redis_connection


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        """
        # 请求中需要包含header为api-token的认证信息,该函数进行认证
        :param request:
        :return:
        """
        token_value = request.META.get("HTTP_API_TOKEN")
        if token_value:
            conn = get_redis_connection('default')
            """:type :redis.client.Redis"""
            username = conn.get(token_value)
            if username:
                token_obj = models.UserInfo.objects.filter(username=str(username, encoding='utf8')).first()
                if not token_obj:
                    raise exceptions.AuthenticationFailed("用户认证失败")
                # 返回request.user 和request.auth
                # return token_obj.user, token_obj
                return token_obj, token_value
            else:
                raise exceptions.AuthenticationFailed("用户认证失败")
        else:
            raise exceptions.AuthenticationFailed("用户认证失败")

    def authenticate_header(self, request):
        pass
