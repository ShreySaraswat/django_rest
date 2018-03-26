from rest_framework import generics
from .serializers import BucketlistSerializer
from .permissions import IsOwner
from .models import Bucketlist
from rest_framework import permissions

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


    def perform_create(self, serializer):
            """Save the post data when creating a new bucketlist."""
            serializer.save(owner=self.request.user) # Add owner=self.request.user

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
