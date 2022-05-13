from rest_framework import serializers
from news.models import Article, Creator
from datetime import datetime
from django.utils.timesince import timesince
from datetime import date



class ArticleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('__all__')
        read_only_fields = [
            'id',
            'create_time',
            'update_time'
        ]
    def get_time_since_pub(self, object):
        now = datetime.now()
        publication_date = object.publish_date
        if object.is_active == True:
            time_delta = timesince(publication_date, now)
            return time_delta
        return 'Not active.'
        
    def validate_publication_date(self, date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError(
                'Publish date cannot be greater than today'
            )
        return date_value

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and description cannot be same.'
            )
        return data
    
    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                'Title should be at least 10 characters.'
            )
        return value
    
    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                'Description should be at least 20.'
            )
        return value



class CreatorSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True) # read_only=True dedigimiz icin article vermeden author yaratabildik.
    articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail',    
    )       # o creator'in article larini url seklinde aldik ama views.py da get function una dikkat et context eklemek zorundayiz.
    class Meta:
        model = Creator
        fields = '__all__'

