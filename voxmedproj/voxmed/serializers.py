from rest_framework import serializers
from .models import Member, Report, ReportPicture, Field, Template, Keyword

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'email', 'password', 'picture_url', 'age', 'registered_time', 'status', 'role', 'patientID', 'fcm_token')

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'member_id', 'subject', 'patientID', 'body', 'picture_url', 'audio_url', 'date_time', 'status')

class ReportPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportPicture
        fields = ('id', 'report_id', 'picture_url')


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'member_id', 'report_id', 'title', 'content', 'status')


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'member_id', 'name', 'items_count')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'template_id', 'keyword')















































