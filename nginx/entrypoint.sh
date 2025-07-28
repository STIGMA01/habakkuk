#!/bin/sh
set -e

echo "Starting nginx service..."

# envsubst '${NGINX_HOST}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

chown -R nginx:nginx /var/log/nginx /var/cache/nginx

exec nginx -g 'daemon off;'

