FROM python:3.9

RUN uname -a
RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN  apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt /tmp/requirements.txt
COPY blog/ src/
# COPY . src/

RUN pip install -r /tmp/requirements.txt

CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]

# EXPOSE 8000
