from unittest.mock import Mock, patch

import pytest
from django.urls import reverse
from rest_framework import status

from ..models import HotelRoom


@pytest.mark.django_db
class TestHotelViews:
    def test_create_room_success(self, client):
        data = {"description": "Luxury Suite", "price_per_night": "200.00"}

        with patch("src.hotels.views.HotelRoom.objects.create") as mock_create:
            mock_room = Mock()
            mock_room.id = 1
            mock_create.return_value = mock_room

            response = client.post(reverse("create_room"), data=data)

            assert response.status_code == status.HTTP_201_CREATED
            assert response.data == {"room_id": 1}

    def test_list_rooms_success(self, client):
        HotelRoom.objects.create(description="Room 1", price_per_night=100.00)
        HotelRoom.objects.create(description="Room 2", price_per_night=150.00)

        response = client.get(reverse("list_rooms"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
