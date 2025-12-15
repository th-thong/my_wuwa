from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views  import APIView
from rest_framework.response import Response
import requests


def get_convene_log_response(url):
    try:
        response = requests.get(url)
        
        # Kiểm tra nếu thành công (Status Code 200)
        if response.status_code == 200:
            data = response.json() # Chuyển đổi kết quả về dạng Dictionary/List
            print("Tiêu đề:", data['title'])
        else:
            print("Lỗi:", response.status_code)

    except Exception as e:
        print("Có lỗi xảy ra:", e)


class ConvenesLogView():
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = request.data.get('url')
        if not url:
            return Response({'error': 'URL not provided'}, status=status.HTTP_400_BAD_REQUEST)

        