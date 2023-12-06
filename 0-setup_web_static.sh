#!/usr/bin/env bash
# sets up my web servers for deployment

sudo apt-get -y -q install nginx > /dev/null
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

sudo sed -i -e '/server_name _;/{ a\n
        \n
        location /hbnb_static/ {\n
                alias /data/web_static/current/;\n
        }
}' /etc/nginx/sites-available/default

sudo systemctl restart nginx
