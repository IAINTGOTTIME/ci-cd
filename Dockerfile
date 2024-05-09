FROM python:3.12-alpine

RUN pip install pipenv

COPY .. .

RUN pipenv install --deploy --system

ENV PATH="/.venv/bin:$PATH"

CMD ["sh","-c", "pytest -n 4"]


