from rest_framework import authentication
from core.jwt import get_token_user, get_token
from rest_framework.authentication import SessionAuthentication


class BaseSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        pass

# jwt 토큰 인증


class JWTAuthentication(authentication.SessionAuthentication):
    def authenticate(self, request):

        token = get_token(request)
        user = get_token_user(token)

        # self.enforce_csrf(request)

        return (user, None)
