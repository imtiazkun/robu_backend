from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Applicant
from .serializers import ApplicantsSerializer, ApplicantsSerializer2, InterviewSerializer

class IsAdminOrInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin or president
        return request.user.is_admin_or_panel or request.user.is_admin_or_dads

class ApplicantsCreateView(generics.CreateAPIView):
    serializer_class = ApplicantsSerializer2
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user field from the request's authenticated user
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Override create method to customize the response
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ApplicantsUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantsSerializer2
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Override update method to customize the response
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ApplicantsDeleteView(generics.DestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantsSerializer2
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        # Override destroy method to customize the response
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicantsInfoView(generics.ListAPIView):
    serializer_class = ApplicantsSerializer2
    permission_classes = [IsAuthenticated,IsAdminOrInterviewer]

    def get_queryset(self):
        user_id = self.request.user.id
        return Applicant.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': applicant.id} for applicant in queryset]
        return Response(data)
    

class InterviewUpdateView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Applicant.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated, IsAdminOrInterviewer]
    lookup_field = 'custom_id'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)