FROM python:3.12-alpine

RUN pip install pipenv

RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata

COPY . .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

ENV PATH="/.venv/bin:$PATH"

CMD ["sh", "-c", "pytest -s -v --alluredir allure-results tests/test_login.py", "allure serve allure-results"]