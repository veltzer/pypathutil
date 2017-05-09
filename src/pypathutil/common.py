import os


def is_exe(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)


def add(
        folder: str,
        path: str,
        head: bool,
        separator: str=os.pathsep,
        remove_duplicates: bool=True,
        remove_non_folders: bool=True,
        remove_non_abs: bool=True,
):
    folder = clean(
        folder,
        separator,
        remove_duplicates=remove_duplicates,
        remove_non_folders=remove_non_folders,
        remove_non_abs=remove_non_abs,
    )
    path_elements = path.split(separator)
    if folder != "":
        if head:
            path_elements.insert(0, folder)
        else:
            path_elements.append(folder)
    new_path = separator.join(path_elements)
    new_path = clean(
        new_path,
        separator,
        remove_duplicates=remove_duplicates,
        remove_non_folders=remove_non_folders,
        remove_non_abs=remove_non_abs,
    )
    return new_path


def do_remove_non_abs(path: str, separator: str=os.pathsep):
    return separator.join([x for x in path.split(separator) if os.path.isabs(x)])


def do_remove_non_folders(path: str, separator: str=os.pathsep):
    return separator.join([x for x in path.split(separator) if os.path.isdir(x)])


def do_remove_duplicates(path: str, separator: str=os.pathsep):
    s = set()
    l = []
    for path_element in path.split(separator):
        if path_element not in s:
            s.add(path_element)
            l.append(path_element)
    return separator.join(l)


def clean(
        path: str,
        separator: str=os.pathsep,
        remove_duplicates: bool=True,
        remove_non_folders: bool=True,
        remove_non_abs: bool=True,
):
    """
    returns a reduced version of the path. This means without repetition and without parts
    which are not folders.
    :param remove_non_abs: 
    :param remove_non_folders: 
    :param remove_duplicates: 
    :param path: 
    :param separator: 
    :return: 
    """
    if remove_duplicates:
        path = do_remove_duplicates(path, separator)
    if remove_non_folders:
        path = do_remove_non_folders(path, separator)
    if remove_non_abs:
        path = do_remove_non_abs(path, separator)
    return path


def find_in_path(path: str, app: str, separator: str=os.pathsep, strict: bool=False):
    """
    Return the full path if found, None otherwise
    :param path: 
    :param app: 
    :param separator: 
    :param strict: 
    :return: 
    """
    for path_element in path.split(separator):
        if strict:
            assert os.path.isabs(path_element), "Not absolute"
            assert os.path.isdir(path_element), "Not a folder"
        full_path_app = os.path.join(path_element, app)
        if is_exe(full_path_app):
            return full_path_app
    return None
