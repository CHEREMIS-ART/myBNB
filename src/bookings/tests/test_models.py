from datetime import date

import pytest
from django.core.exceptions import ValidationError

from src.hotels.models import HotelRoom

from ..models import Booking


@pytest.mark.django_db
class TestBookingModel:
    def test_create_booking(self):
        room = HotelRoom.objects.create(description="Test Room", price_per_night=100.00)
        booking = Booking.objects.create(
            room=room, date_start=date(2024, 1, 1), date_end=date(2024, 1, 5)
        )
        assert booking.id is not None
        assert booking.room == room

    def test_booking_date_validation(self):
        room = HotelRoom.objects.create(description="Test Room", price_per_night=100.00)
        booking = Booking(
            room=room, date_start=date(2024, 1, 5), date_end=date(2024, 1, 1)
        )
        with pytest.raises(ValidationError):
            booking.full_clean()
