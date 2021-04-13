from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from K.permissions import IsOwner, ReadOnly
from .models import Event, Option
from .serializers import EventSerializer, OptionSerializer


class EventListCreateAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, ReadOnly | IsOwner)


class OptionCreateAPIView(CreateAPIView):
    serializer_class = OptionSerializer
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        event = self.get_object()
        serializer.save(event=event)


class OptionDeleteAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        Option.objects.filter(event__owner=self.request.user)


class VoteCreateDeleteAPIView(CreateAPIView, DestroyAPIView):
    queryset = Option.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        option = self.get_object()
        option.voters.add(request.user)
        option.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, option):
        option.voters.remove(self.request.user)
        option.save()
