import os


def unislash(s):
    if os.name == "nt":
        return s.replace("\\", "/")
    else:
        return s