#!/usr/bin/python3

''' Distributes an archive to my web servers '''

from fabric.api import run, put, settings
from paramiko.pkey import PKey
import os
import sys


def do_deploy():
    ''' deployes the archived files to the web servers '''
    
    
    env = os.environ
    env.key_filename = "~/.ssh/school.pem"
    env.hosts = ['54.146.81.93', '34.232.76.218']
    env.user = 'ubuntu'

    for host in env.hosts:
        with settings(host_string=host):
            archive_path = 'versions/web_static_20231207141839.tgz'
            archive_name = 'web_static_20231207141839.tgz'
            dir_name = archive_name[:-4]
            results = []

            if not(os.path.exists(archive_path)):
                return False

            # Upload files to the server
            put(archive_path, "/tmp")
            with run('cd /tmp'):
                archive_path = 'versions/web_static_20231207141839.tgz'
                archive_name = 'web_static_20231207141839.tgz'
                dir_name = archive_name[:-4]
                results = []

                # Make a dir for the files to be unarchived
                results.append(run(f'mkdir -p /data/web_static/releases/{dir_name}'))
                # Unarchive files into the designates folder
                results.append(run(f'tar -xzf /tmp/{archive_name} -C'
                               + '/data/web_static/releases/'+'{dir_name}/'))
                # Remove .tgz file
                results.append(run(f'rm -rf /tmp/{archive_name}'))
                # Move the static files to the desired folder
                results.append(run(f'mv /data/web_static/releases/{dir_name}/web_static/*'
                + '/data/web_static/releases/{dir_name}'))
                # Remove emptied folder
                results.append(run(f'rm -rf /data/web_static/releases/{dir_name}/web_static'))
                # Removes existing symbolic link
                results.append(run(f'rm -rf /data/web_static/current'))
                # Create new symbolic link
                results.append(run(f'ln -s /data/web_static/releases/{dir_name}'
                + '/data/web_static/current'))

                if None in results or 0 in results:
                    return False
                else:
                    return True
