from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from useraccount.manager import UserAccountManager

from django.utils.translation import ugettext_lazy as _

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    | Field    | Details |
    | :------- | :------ |
    | username | 32 chars, unique |
    | password | 128 chars |
    | root     | TreeNode fk |
    """

    username = models.CharField(
        _('username'),
        max_length=32,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    root = models.OneToOneField(
        'filesystem.TreeNode',
        verbose_name=_('root'),
        on_delete=models.CASCADE,
        null=True,
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __str__(self):
        return self.username