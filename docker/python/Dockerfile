FROM python:3.12
WORKDIR /var/www/flask1
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip
RUN pip install flask
CMD ["python", "-m", "flask", "run", "--debug", "--host=0.0.0.0"]
