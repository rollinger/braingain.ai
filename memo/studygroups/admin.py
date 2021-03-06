from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from flashcards.models import Card, Topic
from studygroups.models import Membership, StudyGroup


class TopicsInline(admin.TabularInline):
    model = Topic
    fk_name = "group"
    ordering = ("-title",)
    extra = 0
    fields = ("title",)


class MembershipInline(admin.TabularInline):
    model = Membership
    fk_name = "group"
    ordering = ("-role",)
    extra = 0
    fields = (
        "member",
        "role",
        "approved",
        "blocked",
        "created_at",
        "updated_at",
    )
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = ["member"]
    # verbose_name_plural = "Predisposed by:"


class CardsInline(admin.StackedInline):
    model = Card
    fk_name = "group"
    ordering = ("-created_at",)
    extra = 0
    fields = ("topic", "front_text", "back_text")


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "name",
        "slug",
        "auto_approve_new_member",
        "is_main_user_group",
        "is_publicly_available",
        "get_card_count",
    )
    list_display_links = ("name",)
    list_filter = (
        "auto_approve_new_member",
        "is_main_user_group",
        "is_publicly_available",
    )
    readonly_fields = [
        "id",
        "unique_id",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {"slug": ("name",)}
    # autocomplete_fields = ["memoset"]
    inlines = [
        MembershipInline,
        TopicsInline,
        CardsInline,
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "name",
                        "slug",
                    ),
                    "description",
                )
            },
        ),
        (
            "Group Settings",
            {
                "classes": ("extrapretty",),
                "fields": (
                    ("auto_approve_new_member", "new_member_role"),
                    ("is_main_user_group", "is_publicly_available"),
                ),
            },
        ),
        (
            "System Information",
            {
                "classes": ("collapsible",),
                "fields": ("id", "unique_id", "created_at", "updated_at"),
            },
        ),
    )

    def get_card_count(self, obj):
        return obj.number_cards()

    get_card_count.short_description = _("Cards")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "group",
        "member",
        "role",
        "approved",
        "blocked",
    )
    list_display_links = ("member",)
    list_filter = (
        "approved",
        "blocked",
        "role",
    )
    readonly_fields = [
        "id",
        "unique_id",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "group",
        "member",
    ]
    autocomplete_fields = ["group", "member"]
