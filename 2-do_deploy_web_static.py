#!/usr/bin/python3

''' Distributes an archive to my web servers '''

from fabric.api import run, put, env
import os

env.hosts = ['54.146.81.93', '34.232.76.218']


def do_deploy(archive_path):
    ''' deployes the archived files to the web servers '''

    try:
        # Upload files to the server
        put(archive_path, "/tmp")

        archive_name = archive_path[9:]
        dir_name = archive_name[:-4]

        # Make a dir for the files to be unarchived
        run(f'mkdir -p /data/web_static/releases/{dir_name}')
        # Unarchive files into the designated folder
        run(f'tar -xzf /tmp/{archive_name} -C'
            + f' /data/web_static/releases/{dir_name}/')
        # Remove .tgz file
        run(f'rm -rf /tmp/{archive_name}')
        # Move the static files to the desired folder
        run(f'mv /data/web_static/releases/{dir_name}/web_static/* '
            + f'/data/web_static/releases/{dir_name}')
        # Remove emptied folder
        run(f'rm -rf /data/web_static/releases/'
            + f'{dir_name}/web_static')
        # Removes existing symbolic link
        run(f'rm -rf /data/web_static/current')
        # Create new symbolic link
        run(f'ln -s /data/web_static/releases/{dir_name}'
            + ' /data/web_static/current')

        return True
    except Exception as e:
        return False
