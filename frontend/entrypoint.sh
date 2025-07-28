#!/bin/sh

set -e

echo "Starting frontend build..."

npm install
npm run build

echo "Build completed."

exit 0


# if [ ! -d "/app/dist" ]; then
# fi
