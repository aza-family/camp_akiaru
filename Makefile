
install:
	pip3 install -r requirements.txt -t site-packages
install_ci:
	python -m pip install --upgrade pip
	pip install -r requirements.txt -t site-packages
run:
	PYTHONPATH="${PYTHONPATH}:./site-packages" python run.py
run3:
	PYTHONIOENCODING=utf-8 PYTHONPATH="${PYTHONPATH}:./site-packages" env LC_ALL=en_US.UTF-8 /usr/local/bin/python3.9 run.py


# docker run -v $PWD:/home/root/ -e PYTHONPATH="./site-packages" -w /home/root --rm --name camp_akiaru python:3.7.3-alpine3.10 python run.py