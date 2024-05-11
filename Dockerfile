FROM python:3.12-alpine

USER root

RUN addgroup -S app && adduser -S -G app app

RUN pip install pipenv

RUN apk update | \
    apk add --no-cache chromium chromium-chromedriver tzdata

RUN apk update | \
    apk --no-cache add openjdk21

RUN apk --no-cache add curl

RUN apk --no-cache add tar

RUN curl -o allure-2.29.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.29.0/allure-commandline-2.29.0.tgz

RUN tar -zxvf allure-2.29.0.tgz -C /opt/

RUN ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure

RUN allure --version

COPY . .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

ENV PATH="/.venv/bin:$PATH"

CMD ["sh", "-c", "pytest -s -v --alluredir=allure-result test_login.py"]