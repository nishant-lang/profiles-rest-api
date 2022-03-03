
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_api import serializers
from profile_api import models
from rest_framework.authentication import TokenAuthentication
from profile_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer
    
    def get(self,request,format=None):
        """Return a list of ApiView features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delite)',
            'Is simalar to a traditional Django View',
            'Gives t]you the most control over you applications logic',
            'Is mapped manually to URLs'
        ]

        return  Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """"Create a hello message with our name"""
        
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an objects"""
        return Response({'method':'PUT'}) 


    def patch(self,request,pk=None):
        """Handle updating of an objects"""
        return Response({'method':'PATCH'}) 

    def delete(self,request,pk=None):
        """Deliting an objects"""
        return Response({'method':'DELETE'}) 


class HelloViewSet(viewsets.ViewSet):
    """"Test API viewset"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """Return a hello  message"""
        an_viewset=[
            'Uses actions(list,create,retrive,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provide more functionality eith less code'
        ]
        return Response({'message':'Hello','an_viewset':an_viewset})
    
    def create(self,request):
        """Create a new Hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name} !'
            return Response({'message':message})

        else:
            return Response(
                   serializer.errors,
                   status=status.HTTP_400_BAD_REQUEST

            )
    def retrive(self,request,pk=None):
        """Handle getting an object by it's id"""
        return Response ({'http_method':'GET'})


    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an objects"""
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):                                       
    """Handel creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentications_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentications tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handel crating Reading and updating profile feed items"""
    Authentication_classse=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfilefeedItem.objects.all()


    def perform_create(self,seralizer):
        """Set the user profile to the logged in the user"""
        seralizer.save(User_Profile=self.request.user)

