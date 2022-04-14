from django.test import TestCase
from django.contrib.auth.models import User
import json

test_user = {"username": "testuser", "password": "testpassword"}


class PizzasTest(TestCase):
    def setUp(self):
        new_user = User.objects.create(
            username=test_user["username"])
        new_user.set_password(test_user["password"])
        new_user.save()

    def get_token(self):
        res = self.client.post('/api/token/',
                               data=json.dumps({
                                   'username': test_user["username"],
                                   'password': test_user["password"],
                               }),
                               content_type='application/json',
                               )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        return result["access"]

    # UNauthorized users are NOT allowed to POST
    def test_add_toppings_forbidden(self):
        res = self.client.post('/api/pizza-toppings/',
                                data=json.dumps({
                                    'name': "Forbidden Fruit",
                                }),
                                content_type='application/json',
                                )
        self.assertEquals(res.status_code, 401)

        res = self.client.post('/api/pizza-toppings/',
                             data=json.dumps({
                                 'name': "Outlawed Tomato",
                             }),
                             content_type='application/json',
                             HTTP_AUTHORIZATION=f'Bearer WRONG TOKEN'
                             )
        self.assertEquals(res.status_code, 401)

    # authorized users are allowed to POST
    def test_add_toppings_ok(self):
        token = self.get_token()
        res = self.client.post('/api/pizza-toppings/',
                                data=json.dumps({
                                    'name': "Allowed Anchovies",
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 201)
        result = json.loads(res.content)
        self.assertEquals(result["name"], 'Allowed Anchovies')

    def test_add_toppings_wrong_data(self):
        token = self.get_token()
        res = self.client.post('/api/pizza-toppings/',
                                data=json.dumps({
                                    'label': "Wrong Data",
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 400)

    def test_get_records(self):
        token = self.get_token()
        res = self.client.post('/api/pizza-toppings/',
                                data=json.dumps({
                                    'name': "Fabulous Feta",
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 201)
        id1 = json.loads(res.content)["id"]

        res = self.client.post('/api/pizza-toppings/',
                                data=json.dumps({
                                    'name': "Happy Ham",
                                }),
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )
        self.assertEquals(res.status_code, 201)
        id2 = json.loads(res.content)["id"]

        res = self.client.get('/api/pizza-toppings/',
                                content_type='application/json',
                                HTTP_AUTHORIZATION=f'Bearer {token}'
                                )

        self.assertEquals(res.status_code, 200)
        result = json.loads(res.content)
        self.assertEquals(len(result), 2)  # 2 records
        self.assertTrue(result[0]["id"] == id1 or result[1]["id"] == id1)
        self.assertTrue(result[0]["id"] == id2 or result[1]["id"] == id2)
