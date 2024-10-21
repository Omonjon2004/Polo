from django.contrib import admin

from apps.account.models import Users, UsersCards


class UsersCardsTabularInline(admin.TabularInline):
    model = UsersCards
    extra = 1


@admin.register(Users)
class AccountAdmin(admin.ModelAdmin):
    inlines = [UsersCardsTabularInline]
    search_fields = ("email", "phone_number")
    list_display = ("id",
                    "email",
                    "phone_number",
                    "username",
                    "is_active",
                    "is_staff",
                    )
