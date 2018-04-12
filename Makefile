excludes = \*~ \*.pyc .cache/\* test_\* __pycache__/\*

.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete

.PHONY: test
test:
	nosetests --with-cov --cov flask_ses_mailer

.PHONY: bandit
bandit:
	bandit -r flask_ses_mailer/

.PHONY: coveralls
coveralls:
	coveralls
