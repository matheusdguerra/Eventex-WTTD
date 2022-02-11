from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            bady = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                           bady,
                           'matheusguerra@outlook.com',
                           ['matheusguerra@outlook.com', form.cleaned_data['email']])

            messages.success(request, 'Incrição realizada com sucesso!')

            return(HttpResponseRedirect('/inscricao/'))
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
