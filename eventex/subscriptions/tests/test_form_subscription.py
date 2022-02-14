from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class Subscription(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form mus have 4 fields"""
        excpected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(excpected, list(self.form.fields))
