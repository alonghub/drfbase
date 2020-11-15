from django.shortcuts import render
from django.http import JsonResponse
from django_redis import get_redis_connection
from rest_framework.views import APIView
from rest_framework import status
from api import models


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf8'))
    m.update(bytes(ctime, encoding='utf8'))
    return m.hexdigest()


# Create your views here.
class Root(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return JsonResponse({"msg": "ok"}, status=status.HTTP_200_OK)


class AuthView(APIView):
    """
    用户登录认证
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        ret = {"code": 1000, "msg": None}
        try:
            username = request.data["username"]
            password = request.data["password"]
            conn = get_redis_connection('default')
            pass_verify = conn.get(f"{username}_verify")
            if pass_verify:
                if password != str(pass_verify, encoding='utf8'):
                    ret["code"] = 1001
                    ret["message"] = "用户名或密码错误"
                    return JsonResponse(ret, status=status.HTTP_403_FORBIDDEN)
            else:
                obj = models.UserInfo.objects.filter(username=username, password=password).first()
                if not obj:
                    ret["code"] = 1001
                    ret["message"] = "用户名或密码错误"
                    return JsonResponse(ret, status=status.HTTP_403_FORBIDDEN)
                else:
                    conn.set(f"{username}_verify", obj.password, 60 * 5)
            """:type :redis.client.Redis"""
            token = conn.get(username)
            if token:
                conn.expire(username, 60 * 60)
                token = str(token, encoding='utf-8')
                conn.expire(token, 60 * 60)
            else:
                token = md5(username)
                conn.set(username, token, 60 * 60)
                conn.set(token, username, 60 * 60)
            ret["token"] = token
            ret["data"] = {'token': token}
            return JsonResponse(ret)
        except Exception as e:
            print(e)
            ret["code"] = 1002
            ret["msg"] = "请求异常"

        return JsonResponse(ret, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class UserInfo(APIView):
    # authentication_classes = []
    # permission_classes = []
    def get(self, request, *args, **kwargs):
        result = {
            "code": 1000,
            "data": {
                "roles": ["admin"],
                "introduction": "I am a super administrator",
                "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                "name": "Super Admin"
            }
        }
        return JsonResponse(result, status=status.HTTP_200_OK)
