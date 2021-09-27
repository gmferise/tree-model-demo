from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from filesystem.models import TreeNode

admin.site.register(
    TreeNode,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'is_file',
    ),
    list_display_links=(
        'indented_title',
    ),
)