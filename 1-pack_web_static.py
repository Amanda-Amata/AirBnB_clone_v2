#!/usr/bin/python3
""" A fabric script to Generates a .tgz archive from
    the contents of the web_static folder """

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """ generates a .tgz archive from web_static"""

    
    time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second)

    if os.path.isdir("version") is False:
        if local('mkdir -p version').failed is True:
            return None
    if local('tar -cvzf {} web_static'.format(file)).failed is True:
        return None
    return file
