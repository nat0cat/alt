from django.test import TestCase
from django.urls import reverse


class APITestCase(TestCase):
    def test_get_request_returns_correct_response(self):
        # Make a GET request to your API endpoint
        response = self.client.get(reverse('http://127.0.0.1:8000/result/8/'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {
                "id": 20,
                "score": 2,
                "count": 1,
                "num_questions": 1,
                "user": 8,
                "assessment": 1
            }
        ]

        # Optionally, check the response content or other attributes
        # self.assertEqual(response.json(), expected_data)

    def test_post_request_returns_correct_response(self):
        # Define the request data
        data = {'user_id': '8', 
                'response': 'omg', 
                }

        # Make a POST request to your API endpoint
        response = self.client.post(reverse('http://127.0.0.1:8000/response/6/'), data=data)

        # Check that the response status code is 201 (Created) or as expected
        self.assertEqual(response.status_code, 201)

        # expected_data = [
        #     {
        #         "id": 23,
        #         "num": 2,
        #         "count": 1,
        #         "user": 8,
        #         "question": 6
        #     }
        # ]
        # Optionally, check the response content or other attributes
        # self.assertEqual(response.json(), expected_data)

    # Add more test cases for other types of requests (PUT, DELETE, etc.) as needed
