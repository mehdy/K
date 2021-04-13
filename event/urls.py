from django.urls import path

from .apis import (
    EventListCreateAPIView,
    EventRetrieveUpdateDestroyAPIView,
    OptionDeleteAPIView,
    OptionCreateAPIView,
    VoteCreateDeleteAPIView,
)

urlpatterns = [
    path("option/<str:pk>/", OptionDeleteAPIView.as_view(), name="option-delete"),
    path("option/<str:pk>/vote/", VoteCreateDeleteAPIView.as_view(), name="vote-create-delete"),
    path("<str:pk>/option/", OptionCreateAPIView.as_view(), name="option-create"),
    path("<str:pk>/", EventRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-destroy"),
    path("", EventListCreateAPIView.as_view(), name="list-create"),
]
