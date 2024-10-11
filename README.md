# DynamoDB Query Lambda Functions

This project demonstrates two AWS Lambda functions (one in Python and one in Go) that query a DynamoDB table and return the results. The project includes Terraform scripts for deploying the necessary AWS resources.  These might be used in comparing the relative performance of Go vs. Python in an AWS Lambda environment.

## Project Structure

```
/
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── providers.tf
│
├── src/
│   ├── python/
│   │   └── lambda_function.py
│   │
│   └── go/
│       ├── main.go
│       └── go.mod
│
├── build/
│   ├── python_lambda.zip
│   └── go_lambda.zip
│
├── lambda-zip-python.sh
├── lambda-zip-go.sh
└── README.md
```

## Lambda Functions

### Python Lambda

The Python Lambda function uses boto3 to query the DynamoDB table. It expects a `user_id` as a query parameter and returns the corresponding user data in JSON format.

### Go Lambda

The Go Lambda function uses the AWS SDK for Go to query the DynamoDB table. Like the Python version, it expects a `user_id` as a query parameter and returns the corresponding user data in JSON format.

## Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform installed
- Python 3.9 or later
- Go 1.x or later

## Creating Lambda Zip Files

Two shell scripts are provided to create the necessary zip files for Lambda deployment:

### Python Lambda

Run the following command:

```bash
./lambda-zip-python.sh
```

This script does the following:
1. Navigates to the `src/python` directory
2. Creates a virtual environment
3. Installs the required dependencies
4. Zips the Lambda function and its dependencies
5. Moves the zip file to the `build` directory

### Go Lambda

Run the following command:

```bash
./lambda-zip-go.sh
```

This script does the following:
1. Navigates to the `src/go` directory
2. Builds the Go binary for Linux
3. Zips the binary
4. Moves the zip file to the `build` directory

## Deploying with Terraform

To deploy the Lambda functions and associated AWS resources:

1. Navigate to the `terraform` directory:
   ```
   cd terraform
   ```

2. Initialize Terraform:
   ```
   terraform init
   ```

3. Plan the deployment:
   ```
   terraform plan
   ```

4. Apply the Terraform configuration:
   ```
   terraform apply
   ```

   When prompted, type `yes` to confirm the deployment.

5. After successful deployment, Terraform will output the API Gateway URL. You can use this URL to invoke your Lambda functions.

## Testing the Lambda Functions

To test the deployed Lambda functions, use the following curl commands:

For the Python Lambda:
```
curl "https://{api-id}.execute-api.{region}.amazonaws.com/prod/python?user_id={your-user-id}"
```

For the Go Lambda:
```
curl "https://{api-id}.execute-api.{region}.amazonaws.com/prod/go?user_id={your-user-id}"
```

Replace `{api-id}`, `{region}`, and `{your-user-id}` with appropriate values.

## Cleaning Up

To avoid incurring unnecessary AWS charges, remember to destroy the resources when you're done:

```
terraform destroy
```

When prompted, type `yes` to confirm the destruction of resources.

## Troubleshooting

If you encounter any issues:

1. Ensure your AWS CLI is correctly configured with the necessary permissions.
2. Check the CloudWatch logs for each Lambda function for error messages.
3. Verify that the DynamoDB table contains data with the queried user_id.

For further assistance, please open an issue in the project repository.
