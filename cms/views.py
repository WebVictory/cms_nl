from django.db import transaction
from rest_framework import permissions
from .models import Page, ContentVideo
from .serializers import PageSerializer,ContentVideoSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by('id')
    serializer_class = PageSerializer
    permission_classes = [permissions.AllowAny]

    #  атомарное обновлние данных
    @transaction.atomic
    def retrieve(self, request, pk=None):
        from itertools import chain
        page = self.get_object()
        video = page.content_video.all()
        audio = page.content_audio.all()
        text = page.content_text.all()
        related_content = list(chain(video, audio, text))
        for content in  related_content:
            content.counter += 1
            content.save()

        serializer = self.get_serializer(page)
        return Response(serializer.data)