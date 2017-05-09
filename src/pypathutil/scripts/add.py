"""
This script adds two paths together
"""
import os

import click

from pypathutil import common


@click.command()
@click.argument(
    'path',
    type=str,
    required=True,
)
@click.argument(
    'folder',
    type=str,
    required=True,
)
@click.option(
    '--head',
    required=False,
    default=True,
    type=bool,
    help="add to the head of the path?",
)
@click.option(
    '--separator',
    required=False,
    default=os.pathsep,
    type=str,
    help="what is the path separator",
)
@click.option(
    '--remove_duplicates',
    required=False,
    default=True,
    type=bool,
    help="remove duplicate elements from the path",
)
@click.option(
    '--remove_non_folders',
    required=False,
    default=True,
    type=bool,
    help="remove non folder elements from the path",
)
@click.option(
    '--remove_non_abs',
    required=False,
    default=True,
    type=bool,
    help="remove non absolute folder elements from the path",
)
def main(path, folder, head, separator, remove_duplicates, remove_non_folders, remove_non_abs):
    new_path = common.add(
        path=path,
        folder=folder,
        head=head,
        separator=separator,
        remove_duplicates=remove_duplicates,
        remove_non_folders=remove_non_folders,
        remove_non_abs=remove_non_abs,
    )
    print(new_path)

if __name__ == "__main__":
    main()
