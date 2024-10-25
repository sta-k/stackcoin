from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

class TransactionTest(TestCase):
    fixtures = [
       "sample.json",
    ]
    def setUp(self):
        self.client = Client()
        self.url = reverse("home")
    
    def test_login_and_make_transaction(self):
        response = self.client.get(self.url, follow=True) 
        self.assertInHTML('<h2>Log in</h2>', response.content.decode())

        self.client.post(reverse('login'), {'username':'7356775981', 'password':'sumee1910'}, follow=True)
        response = self.client.post(self.url, {"destAddress": "8921513696","amount": "2"})  

        response = self.client.get(self.url, follow=True) 
        self.assertInHTML('<h3 class="text-muted">Balance: $-2</h3>', response.content.decode())
        self.assertEqual(response.status_code, 200)
        
    def test_max_transaction(self):
        self.client.post(reverse('login'), {'username':'8921513696', 'password':'sumee1910'}, follow=True)
        response = self.client.post(self.url, {"destAddress": "8921513696","amount": settings.MAXIMUM_BALANCE})
        self.assertEqual(response.status_code, 400)