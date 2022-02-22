from distutils.log import error
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class Subscription(TestCase):

    def test_form_has_fields(self):
        """Form mus have 4 fields"""
        form = SubscriptionForm()
        excpected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(excpected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accpet digits"""
        form = self.make_validated_form(cpf='ABC45678901')
        self.assertformErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertformErrorCode(form, 'cpf', 'lenghf')

    def assertformErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, fild, msg):
        errors = form.errors
        errors_list = errors[fild]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Matheus Guerra', cpf='12345678901',
                     email='matheusguerra@outlook.com', phone='51-992377111')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return(form)
