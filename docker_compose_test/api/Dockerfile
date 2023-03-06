FROM python:3.8.10-slim

WORKDIR /usr/src

COPY ./ /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
