from django.shortcuts import render
from .serializers import GameAccountSerializer, CreateGameAccountSerializer, ChangeGameAccountInfo
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.views  import APIView
from rest_framework.response import Response
from .models import GameAccount


class GameAccountView(APIView):
    permission_classes= [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        game_accounts = user.game_accounts.all()
        serializer = GameAccountSerializer(game_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CreateGameAccountSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
            uid = request.data.get('uid')

            try:
                game_account = request.user.game_accounts.get(uid=uid)
            except GameAccount.DoesNotExist:
                return Response(
                    {"error": "Game account not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = ChangeGameAccountInfo(instance=game_account, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
                
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        uid = request.data.get('uid')
        
        try:
            game_account = request.user.game_accounts.get(uid=uid)
        except GameAccount.DoesNotExist:
            return Response(
                {"error":"Game account not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        game_account.delete()
        return Response({"message": "Game account deleted successfully"},status=status.HTTP_204_NO_CONTENT)




