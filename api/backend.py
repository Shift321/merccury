import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = "Bearer"

    def authenticate(self, request):
        request.user = None

        auth_headear = authentication.get_authorization_header(request).split()
        auth_headear_prefix = self.authentication_header_prefix.lower()

        if not auth_headear:
            return None
        if len(auth_headear) == 1:
            return None
        elif len(auth_headear) > 2:
            return None

        prefix = auth_headear[0].decode("utf-8")
        token = auth_headear[1].decode("utf-8")

        if prefix.lower() != auth_headear_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = "Invalid authenticated. Could not decode token."
            raise exceptions.AuthenticationFailed(msg)
        try:
            user = User.objects.get(pk=payload["id"])
        except User.DoesNotExist:
            msg = "No user matching this token was found"
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "This user has been deactivated"
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)
