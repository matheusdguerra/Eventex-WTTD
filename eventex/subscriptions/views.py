from django.conf import settings
from django.core import mail
from django.http import Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    # Salva no banco
    # Usando forms.ModelForm
    subscription = form.save()

    # Usando forms.Form
    #subscription = Subscription.objects.create(**form.cleaned_data)

    # send email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    # Success feedback
    # messages.success(request, 'Inscrição realizada com sucesso!')

    return(HttpResponseRedirect('{}{}/'.format(r('subscriptions:new'), subscription.hashid)))


def detail(request, hashid):
    try:
        subscriptions = Subscription.objects.get(hashid=hashid)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscriptions})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
