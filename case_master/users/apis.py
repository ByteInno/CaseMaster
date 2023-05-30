#!/usr/bin/env python
# @Project: CaseMaster
# @Author: zero
# @File name: apis
# @Create time: 2023/5/31 00:47
from rest_framework.views import APIView
from rest_framework import serializers

from case_master.api_midleware.pagination import LimitOffsetPagination
from case_master.users.models import BaseUser


class UserListAPI(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.Serializer):
        class Meta:
            model = BaseUser
            fields = ('id', 'email', 'is_admin')

    def get(self, request):
        pass
