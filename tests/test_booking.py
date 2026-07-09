import pytest
import allure
import json
from utils.api_helper import APIHelper
from configs.config import AUTH_PAYLOAD

def load_data():
    with open("data/booking_data.json") as f:
        return json.load(f)

@allure.feature("Booking")
class TestBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = load_data()
        token_response = APIHelper().get_token(AUTH_PAYLOAD)
        self.token = token_response.json()["token"]
        self.api = APIHelper(token=self.token)

    @allure.story("Get Booking")
    @allure.title("TC001 - Get all bookings")
    def test_get_all_bookings(self):
        response = self.api.get_all_bookings()

        assert response.status_code == 200
        assert len(response.json()) > 0

    @allure.story("Create Booking")
    @allure.title("TC002 - Create new booking")
    def test_create_booking(self):
        response = self.api.create_booking(self.data["validBooking"])

        assert response.status_code == 200
        assert response.json()["booking"]["firstname"] == self.data["validBooking"]["firstname"]
        self.__class__.booking_id = response.json()["bookingid"]

    @allure.story("Get Booking")
    @allure.title("TC003 - Get booking by ID")
    def test_get_booking_by_id(self):
        # Create booking dulu
        create = self.api.create_booking(self.data["validBooking"])
        booking_id = create.json()["bookingid"]

        response = self.api.get_booking_by_id(booking_id)

        assert response.status_code == 200
        assert response.json()["firstname"] == self.data["validBooking"]["firstname"]

    @allure.story("Update Booking")
    @allure.title("TC004 - Update booking")
    def test_update_booking(self):
        # Create booking dulu
        create = self.api.create_booking(self.data["validBooking"])
        booking_id = create.json()["bookingid"]

        response = self.api.update_booking(booking_id, self.data["updatedBooking"])

        assert response.status_code == 200
        assert response.json()["firstname"] == self.data["updatedBooking"]["firstname"]

    @allure.story("Update Booking")
    @allure.title("TC005 - Partial update booking")
    def test_partial_update_booking(self):
        # Create booking dulu
        create = self.api.create_booking(self.data["validBooking"])
        booking_id = create.json()["bookingid"]

        response = self.api.partial_update_booking(booking_id, self.data["partialUpdate"])

        assert response.status_code == 200
        assert response.json()["firstname"] == self.data["partialUpdate"]["firstname"]

    @allure.story("Delete Booking")
    @allure.title("TC006 - Delete booking")
    def test_delete_booking(self):
        # Create booking dulu
        create = self.api.create_booking(self.data["validBooking"])
        booking_id = create.json()["bookingid"]

        response = self.api.delete_booking(booking_id)

        assert response.status_code == 201