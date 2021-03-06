from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import TimestampMixin, UUIDMixin

User = get_user_model()

STUDYGROUP_ROLES = (
    ("viewer", _("Viewer")),  # view_perm
    ("editor", _("Editor")),  # view_perm, update_perm
    ("admin", _("Admin")),  # view_perm, update_perm, create_perm, delete_perm
)


class StudyGroupManager(models.Manager):
    pass


class StudyGroup(UUIDMixin, TimestampMixin, models.Model):
    """
    A study group of users co-learing a subject matter
    """

    # TODO: Define primary language of study group

    class Meta:
        verbose_name = _("Study Group")
        verbose_name_plural = _("Study Groups")
        ordering = ("-is_main_user_group", "name")

    name = models.CharField(
        _("Group Title"),
        help_text=_("Name of the group"),
        max_length=255,
    )
    slug = models.SlugField(
        _("Group Slug"),
        help_text=_("URL part of the study group"),
        max_length=50,
        allow_unicode=True,
        unique=True,
    )
    description = RichTextField(_("Description of Study Group"), max_length=2000)

    is_main_user_group = models.BooleanField(
        _("Main User Group"),
        help_text=_("If this is the main user group"),
        default=False,
    )
    is_publicly_available = models.BooleanField(
        _("Publicly available"),
        help_text=_("Study Group can be joined over the directory"),
        default=True,
    )

    new_member_role = models.CharField(
        _("Default member role"),
        help_text=_("Default role of new member"),
        max_length=20,
        choices=STUDYGROUP_ROLES,
        default="viewer",
    )

    auto_approve_new_member = models.BooleanField(
        _("Automatic Approval"),
        help_text=_("New members are approved automatically"),
        default=False,
    )

    objects = StudyGroupManager()

    def __str__(self):
        return "%s" % (self.name)

    def is_member(self, user):
        # TODO: Refactor, determine usage, where?
        return self.memberships.filter(member=user).exists()

    def membership_for(self, user):
        return self.memberships.filter(member=user).first()

    def number_active_members(self):
        return self.memberships.filter(approved=True, blocked=False).count()

    def number_cards(self):
        return self.cards.count()

    def get_invite_url(self):
        # Returns path to update-view
        return reverse("studygroups:group_invite_view", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        # Returns path to update-view
        return reverse("studygroups:group_detail_view", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class MembershipManager(models.Manager):
    pass


class Membership(UUIDMixin, TimestampMixin, models.Model):
    """
    A membership of a user in a studygroup with permissions
    """

    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")
        unique_together = ("group", "member")
        ordering = ("role", "member")

    group = models.ForeignKey(
        StudyGroup,
        help_text=_("Study Group of the relation"),
        related_name="memberships",
        on_delete=models.CASCADE,
    )

    member = models.ForeignKey(
        User,
        help_text=_("User of the relation"),
        related_name="memberships",
        on_delete=models.CASCADE,
    )

    role = models.CharField(
        _("Role"),
        help_text=_("Member's role in study group"),
        max_length=20,
        choices=STUDYGROUP_ROLES,
        default="viewer",
    )

    approved = models.BooleanField(
        _("Approved"),
        help_text=_("Membership is approved"),
        default=False,
    )

    blocked = models.BooleanField(
        _("Blocked"),
        help_text=_("Membership is blocked"),
        default=False,
    )

    objects = MembershipManager()

    def __str__(self):
        return "%s is %s in %s" % (self.member, self.get_role_display(), self.group)

    def get_score(self):
        # TODO: gets the recall score of all cards
        return "%d %%" % (0)

    def get_absolute_url(self):
        # Returns path to update-view
        pass  # return reverse("memocard_update_view", kwargs={"unique_id": self.unique_id})
