from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.response import Response

from articles.models import Article
# Create your tests here.


class ArticleViewSetTestCase(APITestCase):
    BASE_URL = "articles"

    def setUp(self) -> None:
        self.base_url = "https://example.com"
        articles: list[Article] = [
            Article(url=f"{self.base_url}/{i}") for i in range(0, 4 + 1)
        ]
        Article.objects.bulk_create(articles)

    def test_latest_endpoint(self):
        """
        Should return the 3 latest articles
        """
        url = reverse(f"{self.BASE_URL}-latest")
        response: Response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0].get("url"), f"{self.base_url}/4")
        self.assertEqual(response.data[1].get("url"), f"{self.base_url}/3")
        self.assertEqual(response.data[2].get("url"), f"{self.base_url}/2")
