FROM python:3.9 AS builder_python_blog

RUN /usr/local/bin/python -m pip install --upgrade pip
#RUN  apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM builder_python_blog as builder


COPY blog /srv/project/src
COPY blog/Makefile src/Makefile

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /srv/project
RUN chmod 755 /srv/project
USER admin


# CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]

# EXPOSE 8000
