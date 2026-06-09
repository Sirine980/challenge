from rest_framework import generics, viewsets
from accounts.permissions import IsCandidate, IsRecruiter
from .models import CandidateProfile, Experience
from .serializers import CandidateProfileSerializer, ExperienceSerializer


class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsCandidate]

    def get_object(self):
        profile, _ = CandidateProfile.objects.get_or_create(user=self.request.user)
        return profile


class MyExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [IsCandidate]

    def get_queryset(self):
        return Experience.objects.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile, _ = CandidateProfile.objects.get_or_create(user=self.request.user)
        serializer.save(profile=profile)


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CandidateProfile.objects.all().prefetch_related("experiences")
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsRecruiter]