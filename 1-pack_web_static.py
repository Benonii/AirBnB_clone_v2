#!/usr/bin/python3

''' Archives my static files in a .tgz format '''

from fabric.api import run, local, lcd
from datetime import datetime
import os


def do_pack():
    ''' Retrieves static files from github and archives them '''

    local('mkdir -p versions')
    filename = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local('tar -czvf web_static_{}.tgz web_static'.format(filename))

    if result.succeeded:
        local('mv web_static_{}.tgz versions'.format(filename))
        file_path = os.path.join(os.getcwd(), 'web_static_{}.tgz'.
                                 format(filename))
        return file_path

    else:
        return None
