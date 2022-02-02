

install:
	pip install -r requirements.txt -t site-packages

run:
	PYTHONPATH="${PYTHONPATH}:./site-packages" python run.py