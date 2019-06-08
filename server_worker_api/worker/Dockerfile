FROM python:2.7-alpine

ENV  TZ=Asia/Ho_Chi_Minh

RUN apk update && apk upgrade
RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python


RUN mkdir -p /opt/worker

WORKDIR /opt/worker
RUN pip install -U setuptools
RUN python -m pip install --upgrade pip

ADD ./requirements.txt /opt/worker/requirements.txt
RUN pip install -r requirements.txt

# Copy source code to container
COPY . /opt/worker

EXPOSE 8126

ENTRYPOINT ["python", "manage.py"]

