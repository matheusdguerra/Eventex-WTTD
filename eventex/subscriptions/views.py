from django.conf import settings
from django.core import mail
from django.http import Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseCreateView

# ATÉ AQUI
# ATÉ AQUI 2


class SubscriptionCreate(TemplateResponseMixin, BaseCreateView):
    template_name = 'subscriptions/subscription_form.html'
    form_class = SubscriptionForm

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        # Salva no banco
        # Usando forms.ModelForm
        subscription = form.save()

    # Usando forms.Form
    # subscription = Subscription.objects.create(**form.cleaned_data)

    # send email
        _send_mail('Confirmação de inscrição',
                   settings.DEFAULT_FROM_EMAIL,
                   subscription.email,
                   'subscriptions/subscription_email.txt',
                   {'subscription': subscription})

        # Success feedback
        # messages.success(request, 'Inscrição realizada com sucesso!')

        return(HttpResponseRedirect('{}{}/'.format(r('subscriptions:new'), subscription.hashid)))


new = SubscriptionCreate.as_view()


def detail(request, hashid):
    try:
        subscriptions = Subscription.objects.get(hashid=hashid)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscriptions})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
