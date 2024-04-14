import os
from sys import platform

def get_path(file) -> str:
    path = ""
    if platform == "linux":
        path = f"/app/files/{file}"
    elif platform == "win32":
        basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        path = os.path.join(basedir, f'files/{file}')
    return path