#!/usr/bin/env bash

port="8000"

local_ip="127.0.0.1"
net_ip="$(ipconfig getifaddr en0)"

local_url="http://$local_ip:$port/site"
net_url="http://$net_ip:$port/site"

echo "$local_url"
echo "$net_url"
qrencode -t UTF8 -o - "$net_url"

python3 -m http.server "$port"
