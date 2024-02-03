from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.response import Response

from .models import Study


# Create your tests here.
class StudiesViewSetTestCase(APITestCase):
    BASE_URL = "studies"

    def setUp(self) -> None:
        self.base_url = "https://example.com"
        studies: list[Study] = [
            Study(url=f"{self.base_url}/{i}") for i in range(0, 4 + 1)
        ]
        Study.objects.bulk_create(studies)

    def test_latest_endpoint(self):
        """
        Should return the 3 latest studies
        """
        url = reverse(f"{self.BASE_URL}-latest")
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0].get("url"), f"{self.base_url}/4")
        self.assertEqual(response.data[1].get("url"), f"{self.base_url}/3")
        self.assertEqual(response.data[2].get("url"), f"{self.base_url}/2")
