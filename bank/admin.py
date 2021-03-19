from django.contrib import admin

from bank.models.account import Account
from bank.models.currency import Currency
from bank.models.user import User


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'owner',
    )
    autocomplete_fields = (
        'owner',
    )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('code', 'name'),
        }),
        ('Курсы', {
            'fields': ('rate',)
        })
    )
    list_display_links = (
        'id',
        'code',
    )
    list_display = (
        'id',
        'code',
        'name',
        'rate',
    )
    search_fields = (
        'code',
        'name',
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'username',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
