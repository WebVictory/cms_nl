from rest_framework import routers, serializers, viewsets
from .models import Page, ContentVideo, ContentAudio, ContentText


class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = "__all__"

class ContentAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentAudio
        fields = "__all__"

class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = "__all__"

class PageSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()


    def get_content(self, page):
        content = []
        # Получаем связаные обьекты
        video = ContentVideoSerializer(page.content_video.all(), many=True).data
        audio = ContentAudioSerializer(page.content_audio.all(), many=True).data
        text = ContentTextSerializer(page.content_text.all(), many=True).data
        data = (video+audio+text)
        #сортирум по порядку
        content_order = sorted(data, key=lambda d: d['order'])
        content.append(content_order)
        return content

    class Meta:
        model = Page
        fields = "__all__"