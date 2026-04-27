import os
from pathlib import Path
from odoo import SUPERUSER_ID, models


def get_directory_tree(module_path, prefix=''):
    tree = []
    path = Path(module_path)
    if not path.exists():
        return tree
    
    for item in sorted(path.iterdir()):
        if item.name.startswith('.') or item.name == '__pycache__':
            continue
        if item.is_dir():
            tree.append(f"{prefix}├── {item.name}/")
            tree.extend(get_directory_tree(item, prefix + "│   "))
        else:
            tree.append(f"{prefix}├── {item.name}")
    return tree


def register_command(tree):
    from odoo.cli import Command

    class AcademyTreeCommand(Command):
        def run(self, args):
            module_path = Path(__file__).parent.parent
            print(f"\n{module_path.name}/")
            print('\n'.join(get_directory_tree(module_path)))

    tree.register('academy-tree', AcademyTreeCommand)