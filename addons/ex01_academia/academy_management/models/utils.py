import os
from pathlib import Path
from odoo import models, api, SUPERUSER_ID


def get_directory_tree(path, prefix=''):
    tree = []
    p = Path(path)
    if not p.exists():
        return tree
    for item in sorted(p.iterdir()):
        if item.name.startswith('.') or item.name == '__pycache__':
            continue
        if item.is_dir():
            tree.append(f"{prefix}├── {item.name}/")
            tree.extend(get_directory_tree(item, prefix + "│   "))
        else:
            tree.append(f"{prefix}├── {item.name}")
    return tree


class AcademyUtils(models.Model):
    _name = 'academy.utils'
    _description = 'Academy Utils'

    @api.model
    def print_directory_tree(self):
        module_path = Path(__file__).parent.parent
        tree = [f"{module_path.name}/"]
        tree.extend(get_directory_tree(module_path))
        tree_str = '\n'.join(tree)
        print(f"\n{tree_str}\n")
        return tree_str