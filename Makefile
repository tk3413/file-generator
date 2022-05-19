utest:
	pytest --cov-report term-missing --cov=src test/

etest:
	behave e2e/features

lint:
	./lint.sh

install:
	pip3 install -r requirements.txt
