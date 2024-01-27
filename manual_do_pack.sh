#!/bin/bash

# Create the 'versions' directory if it doesn't exist
mkdir -p versions

# Generate the archive filename
dt=$(date -u +"%Y%m%d%H%M%S")
file="versions/web_static_${dt}.tgz"

# Create the tar gzipped archive
tar -cvzf "${file}" web_static

echo "Archive created: ${file}"
