import json
import unittest
import coverage

cov = coverage.coverage(branch=True)
cov.start()

from flask import Flask
from flask_ses_mailer import SESMailer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['AWS_REGION'] = 'us-east-1'
mailer = SESMailer(app)
mailer.ses_source_email = "john.martin@configure.systems"


class TestSESMailer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        cov.stop()
        cov.report(include='flask_ses_mailer/*', show_missing=True)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_connect(self):
        print dir(mailer)

    def test_message(self):
        to_match = {
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'this is a test'
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'test subject'
                }
            }
        message = mailer.message(
            subject='test subject',
            body='this is a test',
        )
        self.assertEqual(message, to_match)

    def test_message_html(self):
        to_match = {
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': '<b>this is an html test</b>'
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'test subject'
                }
            }
        message = mailer.message(
            subject='test subject',
            body='<b>this is an html test</b>',
            body_type='Html'
        )
        self.assertEqual(message, to_match)

    def test_message_invalid_body_type(self):
        to_match = {
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'this is a test'
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'test subject'
                }
            }
        message = mailer.message(
            subject='test subject',
            body='this is a test',
            body_type='basdklah'
        )
        self.assertEqual(message, to_match)

    def test_destination(self):
        destination = mailer.destination(
            to_addresses='test@example.com'
        )
        self.assertEqual(destination, {'ToAddresses': ['test@example.com']})

    def test_send(self):
        message = mailer.send(
            subject='test send function',
            body='This is the test of the body',
            to_addresses='john.martin@configure.systems'
        )
        self.assertTrue(message)
