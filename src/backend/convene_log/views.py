from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializers import ResponseToConveneLogSerializer
import json

from utils.handle_urls import get_params
from external_services.convene_log_api import get_convene_log



class ConveneLogView(APIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        convenes_log_url = request.data.get('convene_log_url')
        
        if not convenes_log_url:
            return Response({"error":"Convenes url is missing"}, status=status.HTTP_400_BAD_REQUEST)


        for i in range(1,2):

            params=get_params(convenes_log_url)

            convenes_log = get_convene_log(
                api_url="https://gmserver-api.aki-game2.net/gacha/record/query",
                url=convenes_log_url,
                card_pool_type=1
            )


            uid = params.get('player_id')
            user = request.user

            game_account = user.game_accounts.filter(uid=uid).first()
            print(game_account.id)
            if not game_account:
                return Response({"error": "Game account not found"})

            serializer = ResponseToConveneLogSerializer(
                data=convenes_log.get("data",[]), 
                many=True
            )

            if serializer.is_valid():
                result = serializer.save(game_account=game_account)
                if result is None:
                    return Response({"message": "Duplicate ignored"}, status=200)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message":"Update convene log succesfully"}, status=status.HTTP_200_OK)