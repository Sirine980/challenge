from rest_framework import serializers
from .models import CandidateProfile, Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "company", "position", "start_date", "end_date", "description"]


class CandidateProfileSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = CandidateProfile
        fields = [
            "id", "username", "title", "phone", "date_of_birth",
            "location", "bio", "experiences",
            "created_at", "updated_at",
        ]