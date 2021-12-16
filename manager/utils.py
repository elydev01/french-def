import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_abspath(path: list):
    """
    Return correct file path

    Args:
        path (list): List of successive folders to access the file

    Returns:
        str: Correct path of the file
    """

    assert isinstance(path, list), "path must be of type list"
    return os.path.join(BASE_DIR, *path)
