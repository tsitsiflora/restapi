from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User_Details, Trip
from .serializers import DetailSerializer, UserSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(username="", name="", password=""):
        if username != "" and name != "" and password != "":
            Users.objects.create(username=title, name=artist, password=password)

    def setUp(self):
        # add test data
        self.create_user("tsitsiflora", "Tsitsi Munikwa", "pass123")
        self.create_user("sarahmh", "Sarah Mamhiyo", "PASS@111")
        self.create_user("tatalmond", "Tatenda Mushayakarara", "password")
        


class GetAllUsersTest(BaseViewTest):

    def test_get_all_users(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("users-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Users.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)