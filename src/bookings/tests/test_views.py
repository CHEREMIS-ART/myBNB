from datetime import date

import pytest
from django.urls import reverse
from rest_framework import status

from src.hotels.models import HotelRoom

from ..models import Booking


@pytest.mark.django_db
class TestBookingViews:
    def test_create_booking_success(self, client):
        room = HotelRoom.objects.create(description="Test Room", price_per_night=100.00)

        data = {
            "room_id": room.id,
            "date_start": "2024-01-01",
            "date_end": "2024-01-05",
        }

        response = client.post(reverse("create_booking"), data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert "booking_id" in response.data

    def test_create_booking_overlapping_dates(self, client):
        room = HotelRoom.objects.create(description="Test Room", price_per_night=100.00)

        Booking.objects.create(
            room=room, date_start=date(2024, 1, 1), date_end=date(2024, 1, 5)
        )

        data = {
            "room_id": room.id,
            "date_start": "2024-01-03",
            "date_end": "2024-01-07",
        }

        response = client.post(reverse("create_booking"), data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Room is already booked for these dates" in str(response.data)
