from boto3.session import Session
import datetime

session = Session(aws_access_key_id='[your_key_id]',
                  aws_secret_access_key='[your_secret_key]')

def delete_from(resource_name,region,your_bucket_name,date):
    resource = session.resource(resource_name,region)
    my_bucket = resource.Bucket(your_bucket_name)
    results = []
    for obj in my_bucket.objects.all():
        if (obj.last_modified).replace(tzinfo = None) < date:
            results.append(
                my_bucket.delete_objects(
                    Delete={
                        'Objects': [
                            {'Key': obj.key}
                        ]
                    }
                )
            )
    return results

delete_from('ec2','us-west','[YOUR_BUCKET]',datetime.datetime(2019,12,1))