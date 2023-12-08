#!/usr/bin/python3

''' Both archives and deploys static files '''

from fabric.api import run, put
import os

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    ''' Deploys and deploys '''

    archive_path = do_pack()

    if archive_path is None:
        return False
