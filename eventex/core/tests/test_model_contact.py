from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContatModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Matheus Guerra',
            slug='matheus-guerra',
            photo='https://yt3.ggpht.com/IyWvcGyapnygPX_boH9DaHEcg0mq0GJZVQ5iud1zW7danc4sFg-VuOEFzNH83uBKoBxkelYw=s88-c-k-c0x00ffffff-no-rj'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='matheusguerra@outlook.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='51-992377111')
        self.assertTrue(Contact.objects.exists())

    def test_choises(self):
        """Contact kind should be limited to E and P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='matheusguerra@outlook.com')
        self.assertEqual('matheusguerra@outlook.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Matheus Guerra',
            slug='matheus-guerra',
            photo='https://yt3.ggpht.com/IyWvcGyapnygPX_boH9DaHEcg0mq0GJZVQ5iud1zW7danc4sFg-VuOEFzNH83uBKoBxkelYw=s88-c-k-c0x00ffffff-no-rj'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='matheusguerra@outlook.com')
        s.contact_set.create(kind=Contact.PHONE, value='51-992377111')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['matheusguerra@outlook.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['51-992377111']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
