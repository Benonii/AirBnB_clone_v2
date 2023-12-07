#!/usr/bin/env bash
# Sets up my web servers for deployment

sudo apt-get -y install nginx > /dev/null
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/tests/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i -e "/server_name _;/{a\
        \
        location /hbnb_static/ {\
                alias /data/web_static/current/;\
        }
}" /etc/nginx/sites-available/default

sudo systemctl restart nginx
