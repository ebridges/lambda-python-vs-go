import boto3
from faker import Faker
import uuid

# Initialize Faker
fake = Faker()

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Make sure this matches your table name

def generate_user():
    return {
        'user_id': str(uuid.uuid4()),
        'username': fake.user_name(),
        'email': fake.email(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'age': fake.random_int(min=18, max=90),
        'address': {
            'street': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zip_code': fake.zipcode(),
            'country': fake.country()
        },
        'phone_number': fake.phone_number(),
        'registration_date': fake.date_time_this_decade().isoformat()
    }

def populate_table(num_users=1000):
    with table.batch_writer() as batch:
        for _ in range(num_users):
            user = generate_user()
            batch.put_item(Item=user)
            print(f"Added user: {user['username']}")

if __name__ == "__main__":
    print("Starting to populate DynamoDB table...")
    populate_table()
    print("Finished populating DynamoDB table.")