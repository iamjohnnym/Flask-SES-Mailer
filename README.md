[![Build Status](https://travis-ci.org/iamjohnnym/Flask-SES-Mailer.svg?branch=master)](https://travis-ci.org/iamjohnnym/Flask-SES-Mailer)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f71700e731a141f8b67370fce984f577)](https://www.codacy.com/app/iamjohnnym/Flask-SES-Mailer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=iamjohnnym/Flask-SES-Mailer&amp;utm_campaign=Badge_Grade)
# Flask-SES-Mailer

## Overview

A simple Flask extension to send mail from Amazon SES.

## Installation

From PyPi

```
pip install Flask-SES-Mailer
```

From GitHub

```
git clone git@github.com:iamjohnnym/Flask-SES-Mailer.git
```

## Usage

### Invocation

```bash
# Bare necessities for use
from flask import Flask
from flask_ses_mailer import SESMailer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['AWS_REGION'] = 'us-east-1'
app.config['SES_SOURCE_EMAIL'] = "ses-sender@example.com"
mailer = SESMailer(app)

@app.route('/')
def hello_world():
    message = mailer.send(
        subject='test send function',
        body='This is the test of the body',
        to_addresses=''
    )
    return message
```

### Testing
```bash
python setup.py test
# or
make test
```

## Features

Sending mail from Amazon SES from your Flask App!

## Contribute

Do your thing, make some MR's.

## Report Bugs

Please toss up any bugs here:

[Issues](https://github.com/iamjohnnym/Flask-SES-Mailer/issues)
