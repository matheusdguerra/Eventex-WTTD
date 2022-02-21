from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePosValid(TestCase):

    def setUp(self):
        data = dict(name='Matheus Guerra', cpf='12345678901',
                    email='matheusguerra@outlook.com', phone='51-99237-7111')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'matheusguerra@outlook.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['matheusguerra@outlook.com', 'matheusguerra@outlook.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_bady(self):
        email = mail.outbox[0]
        contents = ['Matheus Guerra',
                    '12345678901',
                    'matheusguerra@outlook.com',
                    '51-99237-7111']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
