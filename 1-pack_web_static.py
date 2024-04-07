#!/usr/bin/python3
""" A fabric script to Generates a .tgz archive from
    the contents of the web_static folder """

from fabric.api import local
from datetime import datetime
import os.path
import stat

def do_pack():
    """ generates a .tgz archive from web_static"""

    
    date_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second)
    print("Packing web_static to {}".format(file))
    if os.path.isdir("version") is False:
        if local('mkdir -p version').failed is True:
            return None

    if local('tar -cvzf {} web_static'.format(file)).failed is True:
        return None
    os.chmod(file, stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)

    file_size = os.path.getsize(file)
    print("web_static packed: {} -> {}Bytes".format(file, file_size))
    return file
