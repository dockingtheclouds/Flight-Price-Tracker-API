import boto3


class NotificationManager:

    def __init__(self):
        self.client = boto3.client('sns', region_name='us-east-1')

    def send_sms(self, message):
        self.client.publish(
            PhoneNumber= "YOUR_PHONE_NUMBER_HERE",
            Message=message
        )
