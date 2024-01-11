#!/usr/bin/python3

"""python script that makes an archive.
"""
from datetime import datetime
from os import path
from fabfile import *


def do_pack():
    """packing the files.
    """
    tm = datetime.utcnow()

    file =  "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,dt.month, dt.day, dt.hour, dt.minute, dt.second)

    directory_path = "versions"

    if not os.path.isdir(directory_path):
        try:
            os.makedirs(directory_path)
        except OSError as e:
            return None

    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
