import os

def split_extension(filepath):
    name, extension = os.path.splitext(filepath)
    return extension
