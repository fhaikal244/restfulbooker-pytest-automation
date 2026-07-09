import requests
from configs.config import BASE_URL, HEADERS

class APIHelper:

    def __init__(self, token=None):
        self.base_url = BASE_URL
        self.headers = HEADERS.copy()
        if token:
            self.headers["Cookie"] = f"token={token}"

    # ── Auth ──────────────────────────────────────────

    def get_token(self, payload: dict) -> dict:
        response = requests.post(
            f"{self.base_url}/auth",
            json=payload,
            headers=self.headers
        )
        return response

    # ── Booking ───────────────────────────────────────

    def get_all_bookings(self) -> dict:
        response = requests.get(
            f"{self.base_url}/booking",
            headers=self.headers
        )
        return response

    def get_booking_by_id(self, booking_id: int) -> dict:
        response = requests.get(
            f"{self.base_url}/booking/{booking_id}",
            headers=self.headers
        )
        return response

    def create_booking(self, payload: dict) -> dict:
        response = requests.post(
            f"{self.base_url}/booking",
            json=payload,
            headers=self.headers
        )
        return response

    def update_booking(self, booking_id: int, payload: dict) -> dict:
        response = requests.put(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers=self.headers
        )
        return response

    def partial_update_booking(self, booking_id: int, payload: dict) -> dict:
        response = requests.patch(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers=self.headers
        )
        return response

    def delete_booking(self, booking_id: int) -> dict:
        response = requests.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=self.headers
        )
        return response