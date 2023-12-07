#!/usr/bin/env bash
# sets up my web servers for deployment

sudo apt-get -y update
sudo apt-get -y -q install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Testing" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i'38i\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}\n}' /etc/nginx/sites-available/default

sudo service nginx start
