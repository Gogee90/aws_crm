from django.shortcuts import render
import boto3


session = boto3.Session(profile_name='eb-cli')
client = session.client('rds', 'eu-central-1')
# Create your views here.
def get_db_instances(request):
    response = client.describe_db_instances(
        DBInstanceIdentifier='mymysqlinstance',
    )

    print(response)


def create_db(request):
    response = client.create_db_instance(
        AllocatedStorage=5,
        DBInstanceClass='db.t2.micro',
        DBInstanceIdentifier='mymysqlinstance',
        Engine='MySQL',
        MasterUserPassword='onethousandrubbles1000',
        MasterUsername='Gogen',
    )

    print(response)