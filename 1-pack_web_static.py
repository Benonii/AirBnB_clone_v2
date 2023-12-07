#!/usr/bin/python3

''' Archives my static files in a .tgz format '''

from fabric.api import run
from datetime import datetime
import os


def do_pack():
    ''' Retrieves static files from github and archives them '''

    folder_url = "https://github.com/Benonii/AirBnB_clone_v2/web_static"
    run('mkdir -p versions')
    with (run('cd versions')):
        result = run('git archive --format=tar --output={}.tgz {}'.
                     format(datetime.strftime(datetime.now,
                            filename="%Y%m%d%H%M%S"), folder_url))
        if result == 0:
            file_path = os.path.join(os.getcwd(), filename)
            return file_path
        else:
            return None
