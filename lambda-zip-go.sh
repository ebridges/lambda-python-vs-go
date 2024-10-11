#!/bin/bash

set -e

# create build output folder
mkdir -p build

# Navigate to the Go source directory
cd src/go

# Build the Go binary
GOOS=linux GOARCH=amd64 go build -o main

# Create the zip file
zip -j ../../build/go_lambda.zip main

# Clean up
rm main

echo "Go Lambda zip file created successfully."
