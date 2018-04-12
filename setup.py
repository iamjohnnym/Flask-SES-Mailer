"""
Flask-SES-Mailer
-------------

Flask extension for sending email using AWS Simple Email Service.
"""
from setuptools import setup


setup(
    name='Flask-SES-Mailer',
    version='1.0',
    url='https://github.com/iamjohnnym/Flask-SES-Mailer',
    license='Apache2',
    author='john martin',
    author_email='john.martin@configure.systems',
    description='Flask extension to send mail via AWS Simple Email Service.',
    long_description=__doc__,
    packages=['flask_ses_mailer'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    platforms='any',
    install_requires=[
        'Flask',
        'boto3'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
