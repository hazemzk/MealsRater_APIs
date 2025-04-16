from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny , IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]

class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated,]
    @action(methods = ["POST"], detail = True)
    def rate_meal(self, request, pk=None):
        #creat or updete
        if "stars" in request.data:
            meal = Meal.objects.get(id=pk)
            # username = request.data['username']
            stars = request.data['stars']
            user = request.user
            
            # user = User.objects.get(username=username)
            try:
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                json = {
                    "message": "Rating updated successfully",
                                "result":serializer.data
                                }
                return Response(json, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    "message": "Meal Rate created successfully",
                                "result":serializer.data
                                }
                return Response(json, status=status.HTTP_201_CREATED)
                       
        else: 
            json = {'massage':'stars not provided'}
            return Response(json, status=400)
    
    
class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        response = {
            'massage': 'this is not haw you should create or update rating',  
        }
        return Response(response, status= status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'massage': 'this is not haw you should create or update rating',
        }
        return Response(response, status= status.HTTP_400_BAD_REQUEST)