

install:
	pip install -r requirements.txt -t site-packages
install_ci:
	python -m pip install --upgrade pip
	pip install -r requirements.txt -t site-packages
run:
	PYTHONPATH="${PYTHONPATH}:./site-packages" python run.py