from rest_framework.permissions import BasePermission


class IsCandidate(BasePermission):
    message = "Réservé aux candidats."

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role == "CANDIDATE"
        )


class IsRecruiter(BasePermission):
    message = "Réservé aux recruteurs."

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role == "RECRUITER"
        )