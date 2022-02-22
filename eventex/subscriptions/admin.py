from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscrideb_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')

    def subscrideb_today(self, obj):
        return obj.created_at.date() == now().date()

    subscrideb_today.short_description = 'inscrito hoje?'
    subscrideb_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
