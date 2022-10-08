from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, views, permissions, status, mixins
from core.authentication import BaseSessionAuthentication

# from service.services.auth import KakaoAuthService, AppleAuthService
from core.jwt import get_token_user, get_token, renew_access_token_mall
from models import User
from oauth import Oauth2Enum


class UserSocialSignInView(views.APIView):
    authentication_classes = (
        BaseSessionAuthentication,
    )
    auth_service_map = {
        Oauth2Enum.KAKAO.name: KakaoAuthService,
        Oauth2Enum.APPLE.name: AppleAuthService
    }

    @form_validation(Auth2Serializer)
    def post(self, request, serializer):
        data = serializer.data
        auth_service = self.auth_service_map[data['service_name']]
        auth = auth_service(
            access_token=data['access_token'], service_id=data.get('service_id'))
        user = auth.sign_in()
        if not user:
            raise ValidationError({'access_token': '유효하지 않은 토큰입니다.'})
        login(request, user)

        profile = UserProfileSerializer(user)

        return Response(profile.data)
