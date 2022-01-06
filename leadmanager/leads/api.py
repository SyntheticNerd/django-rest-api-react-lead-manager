from rest_framework.serializers import Serializer
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
# a view set lets us create a full CRUD API (Create, Read, Update, Delete)
# check out the Django Rest Framework Doc Viiewsets


class LeadViewSet (viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
