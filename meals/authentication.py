from rest_framework.authentication import TokenAuthentication

class CutomAuth(TokenAuthentication):
    keyword = 'bearer'
