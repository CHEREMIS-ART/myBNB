import pytest

from ..models import HotelRoom


@pytest.mark.django_db
class TestHotelRoomModel:
    def test_create_room(self):
        room = HotelRoom.objects.create(
            description="Luxury suite with sea view", price_per_night=200.00
        )
        assert room.id is not None
        assert room.description == "Luxury suite with sea view"
        assert room.price_per_night == 200.00

    def test_room_string_representation(self):
        room = HotelRoom(description="Test Room", price_per_night=100.00)
        assert str(room) == f"HotelRoom {room.id}"
