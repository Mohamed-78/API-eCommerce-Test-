from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

def check_existance(model, id, field_name):
    try:
        return model.objects.get(id=id), None
    except model.DoesNotExist:
        return None, {field_name: [f"Le {field_name} n'existe pas"]}


def check_existance_contact(model, contact, field_name):
    try:
        return model.objects.get(contact=contact), None
    except model.DoesNotExist:
        return None, {field_name: [f"Le {field_name} n'existe pas"]}

def token_client(client):
    refresh = RefreshToken.for_user(client)
    return {
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
    }