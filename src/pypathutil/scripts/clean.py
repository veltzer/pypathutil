"""
This script cleans a path, removing elements which repeat or are not valid paths
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
def main(path, separator, remove_duplicates, remove_non_folders, remove_non_abs):
    path = common.clean(
        path=path,
        separator=separator,
        remove_duplicates=remove_duplicates,
        remove_non_folders=remove_non_folders,
        remove_non_abs=remove_non_abs,
    )
    print(path)


if __name__ == "__main__":
    main()
