from rest_framework import permissions, viewsets
from .models import Menu, Booking, User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Protected view
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

# ViewSet for Menu to handle single item retrieval
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()  # All menu items in the database
    serializer_class = MenuSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """
        Override the default retrieve method to handle getting a single menu item.
        This is automatically handled by `ModelViewSet`, but you can override if needed.
        """
        return super().retrieve(request, *args, **kwargs)

# ViewSet for Booking
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# ViewSet for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
