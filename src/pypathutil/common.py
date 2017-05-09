import os


def is_exe(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)


def add(folder: str, path: str, head: bool, separator: str=os.pathsep, clean: bool=True):
    path_elements = path.split(separator)
    if clean:
        path_elements = [x for x in path_elements if os.path.isdir(x) and os.path.isabs(x)]
    if not clean or os.path.isdir(folder):
        if head:
            path_elements.insert(0, folder)
        else:
            path_elements.append(folder)
    return separator.join(path_elements)


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
