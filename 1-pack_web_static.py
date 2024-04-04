#!/usr/bin/python3
""" A fabric script to Generates a .tgz archive from
    the contents of the web_static folder """
from fabric.api import *
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from web_static"""
    local('mkdir -p version')
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
