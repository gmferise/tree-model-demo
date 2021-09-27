from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from mptt.exceptions import InvalidMove

from django.utils.translation import ugettext_lazy as _

class TreeNodeManager(TreeManager):
    """
    Prevents incorrect tree-ing in the drag/drop admin panel
    """
    def move_node(self, node, target, position):
        if target.is_file and 'child' in position:
            raise InvalidMove(f'{target} is not a folder')
        super().move_node(node, target, position)

class TreeNode(MPTTModel):
    name = models.CharField(max_length=128)
    is_file = models.BooleanField(default=False)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name=_('children'),
        null=True,
        blank=True,
    )

    objects = TreeNodeManager()

    class MPTTMeta:
        order_insertion_by = ['is_file', 'name']

    def clean(self):
        """
        Prevents incorrect tree-ing on db object creation
        """
        if self.parent and self.parent.is_file:
            raise ValidationError('Parent must be a folder')
        return super().clean()

    def __str__(self):
        return self.name