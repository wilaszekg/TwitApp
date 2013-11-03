from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from TwitApp.settings import SOCIAL_AUTH_LOGIN_ERROR_URL


class SocialAuthCustomMiddle (SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        return SOCIAL_AUTH_LOGIN_ERROR_URL
        #return super(SocialAuthCustomMiddle, self).get_redirect_uri(request, exception)

    def get_message(self, request, exception):
        return super(SocialAuthCustomMiddle, self).get_message(request, exception)