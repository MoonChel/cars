FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

COPY requirements/* /app/requirements/

    # install build and run libs into temporary folders
RUN apk add --no-cache --virtual=.build-deps build-base curl libffi-dev && \
    apk add --no-cache --virtual=.run-deps make libffi && \
    # install requirements
    pip install --no-cache-dir -r requirements/all.txt && \
    # cleanup
    apk del .build-deps && \
    apk del .run-deps

COPY . /app

USER nobody

CMD [ "uvicorn", "run:app" ]
EXPOSE 8080
