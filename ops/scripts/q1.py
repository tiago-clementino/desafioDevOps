from boto3.session import Session

session = Session(aws_access_key_id='[your_key_id]', aws_secret_access_key='[your_secret_key]')

def shutdown_all(credentials_name,region):
    resource = session.resource(credentials_name, region_name=region)
    instances = resource.instances.filter(
        Filters=[{'Values': ['running']}]
    )
    resource.stop_instances(InstanceIds=instances)

shutdown_all('ec2','us-west')