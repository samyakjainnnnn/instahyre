from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import User, Contact
from .serializers import UserSerializer, ContactSerializer
from rest_framework.decorators import action
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to create an account

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def mark_as_spam(self, request, pk=None):
        contact = self.get_object()
        contact.is_spam = True
        contact.save()
        return Response({'status': 'contact marked as spam'})

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(Q(username__icontains=query) | Q(phone_number__icontains=query))

class ContactSearchView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Contact.objects.filter(Q(name__icontains=query) | Q(phone_number__icontains=query))
