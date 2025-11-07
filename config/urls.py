from django.urls import include, path

urlpatterns = [
    path("rooms/", include("src.hotels.urls")),
    path("bookings/", include("src.bookings.urls")),
]
