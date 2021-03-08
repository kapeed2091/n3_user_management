import boto3
from botocore.exceptions import ClientError
from django.conf import settings


def send_email(sender, recipient, subject, body):
    # TODO: Should we use https://github.com/anymail/django-anymail instead of this func?
    CHARSET = "UTF-8"

    client = boto3.client(
        "ses",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )

    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    recipient,
                ],
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": CHARSET,
                        "Data": body,
                    },
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": subject,
                },
            },
            Source=sender,
        )
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response["MessageId"]
