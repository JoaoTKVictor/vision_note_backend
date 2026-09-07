from rest_framework.viewsets import ModelViewSet

from vision.models import Note
from vision.serializers import NoteSerializer

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer