import boto3
from botocore.exceptions import ClientError

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class SESMailer(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.ses_charset = self.app.config.get("SES_CHARSET") or 'UTF-8'
        self.aws_region = self.app.config.get("AWS_REGION") or 'us-west-2'
        self.ses_source_email = self.app.config.get("SES_SOURCE_EMAIL")
        self.client = self._connect()

    def _connect(self):
        self.client = boto3.client('ses', region_name=self.aws_region)
        return self.client

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'ses_connection'):
                ctx.ses_connection = self._connect()
            return ctx.ses_connection

    def destination(self, to_addresses=[]):
        address_list = []
        if isinstance(to_addresses, str):
            address_list.append(to_addresses)
        return { 'ToAddresses': address_list }

    def message(self, subject, body, body_type='Text'):
        message = {}
        message.update(self._subject(subject))
        message.update(self._body(body, body_type))
        return message

    def _body(self, body, body_type='Text'):
        """ Returns a dict to match SES's body model. if you specify
        body_Type="Html", it will send an email with valid html rendering.
        """
        if not body_type in ['Text', 'Html']:
            body_type = 'Text'
        body = {
            'Body': {
                body_type: {
                    'Charset': self.ses_charset,
                    'Data': body
                }
            }
        }
        return body

    def _subject(self, subject):
        return {
            'Subject': {
                'Charset': self.ses_charset,
                'Data': subject
            }
        }

    def send(self, subject, body, to_addresses, body_type='Text', **kwargs):
        # Try to send the email.
        try:
            message = self.message(
                subject=subject,
                body=body,
                body_type=body_type
            )
            #Provide the contents of the email.
            response = self.client.send_email(
                Destination=self.destination(to_addresses),
                Message=message,
                Source=self.ses_source_email
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['ResponseMetadata']['RequestId']
