from django.http
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("로그인 아이디와 패스워드를 확인해주세요.")