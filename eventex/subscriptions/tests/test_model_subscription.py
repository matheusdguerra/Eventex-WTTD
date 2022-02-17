from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Matheus Guerra',
            cpf='12345678901',
            email='matheusguerra@outlook.com',
            phone='51-992377111'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto create_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def teste_str(self):
        self.assertEqual('Matheus Guerra', str(self.obj))
