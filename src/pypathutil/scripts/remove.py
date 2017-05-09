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
    '--separator',
    required=False,
    default=os.pathsep,
    type=str,
    help="what is the path separator",
)
@click.option(
    '--remove_duplicates/--no_remove_duplicates',
    required=False,
    default=True,
    help="remove duplicate elements from the path",
)
@click.option(
    '--remove_non_folders/--no_remove_non_folders',
    required=False,
    default=True,
    help="remove non folder elements from the path",
)
@click.option(
    '--remove_non_abs/--no_remove_non_abs',
    required=False,
    default=True,
    help="remove non absolute folder elements from the path",
)
def main(path, folder, separator, remove_duplicates, remove_non_folders, remove_non_abs):
    new_path = common.remove(
        path=path,
        folder=folder,
        separator=separator,
        remove_duplicates=remove_duplicates,
        remove_non_folders=remove_non_folders,
        remove_non_abs=remove_non_abs,
    )
    print(new_path)

if __name__ == "__main__":
    main()
