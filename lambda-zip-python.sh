#!/bin/bash

set -e

# create build output folder
mkdir -p build

# Navigate to the Python source directory
cd src/python

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install boto3

# Create a temporary directory for the package
mkdir -p package

# Copy the Lambda function to the package directory
cp lambda_function.py package/

# Install dependencies into the package directory
pip install -r requirements.txt -t package/

# Create the zip file
cd package
zip -r ../../build/python_lambda.zip .

# Clean up
cd ..
rm -rf package
deactivate

echo "Python Lambda zip file created successfully."
