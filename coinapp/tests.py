from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

class TransactionTest(TestCase):
    fixtures = [
       "sample.json",
    ]
    def setUp(self):
        self.client = Client()
        self.url = reverse("coinapp:home")
    
    def test_login_and_make_transaction(self):
        response = self.client.get(self.url, follow=True) 
        self.assertInHTML('<h2>Log in</h2>', response.content.decode())

        # login as sulaiman and make a payment 10$(offering 1: Matta rice) -> nusra
        self.client.post(reverse('login'), {'username':'8547622462', 'password':'sumee1910'}, follow=True)
        response = self.client.post(self.url, {"touser": "8921513696","offering": "1"})  

        response = self.client.get(self.url) 
        # check sulaiman has -10$ balance
        self.assertInHTML('<h3 class="text-muted">Balance: -10$</h3>', response.content.decode())
        
        # login as nusra. check she has 10$ balance
        response = self.client.post(reverse('login'), {'username':'8921513696', 'password':'sumee1910'}, follow=True)
        self.assertInHTML('<h3 class="text-muted">Balance: 10$</h3>', response.content.decode())
        
        
    def test_max_transaction(self):
        self.client.post(reverse('login'), {'username':'8547622462', 'password':'sumee1910'}, follow=True)
        response = self.client.post(self.url, {"touser": "8547622462","offering": "15"})
        # settings.MAXIMUM_BALANCE exceeded then 400
        self.assertEqual(response.status_code, 400) # settings.MAXIMUM_BALANCE