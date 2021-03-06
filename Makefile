clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;
dist:
	flake8

test:
	openfisca test --country-package openfisca_barcelona openfisca_barcelona/tests

test_remote_debug:
	openfisca-debug-test --debugserver ${DEBUG_SERVER} --country-package openfisca_barcelona openfisca_barcelona/tests

test_verbose:
	openfisca test -v --country-package openfisca_barcelona openfisca_barcelona/tests

run:
	openfisca serve --country-package openfisca_barcelona --port 2000

prod-run:
	openfisca serve  --configuration-file production-config/config.py --port ${PORT}

deploy-heroku:
	git push heroku master
