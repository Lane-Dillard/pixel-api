from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

# Profile ViewSet
class Profile(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()  # Retrieve all users
        serializer = ProfileSerializer(users, many=True)  # Serialize the queryset
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)