#!/usr/bin/env bash
# sets up my web servers for deployment

sudo apt-get -y update > /dev/null
sudo apt-get -y -q install nginx > /dev/null
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo touch /data/web_static/current/index.html
echo "\
<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>" | sudo tee /data/web_static/current/index.html > /dev/null
sudo chown -R ubuntu:ubuntu /data

sudo sed -i -e '/server_name _;/{
        a\
        \
        location /hbnb_static/ {\
                alias /data/web_static/current/;\
        }
}' /etc/nginx/sites-available/default

sudo service nginx start

