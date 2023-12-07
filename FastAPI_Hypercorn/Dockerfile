FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN rm -rf /root/.cache/pip

COPY ./app /app

ENTRYPOINT ["hypercorn", "main:app", "--bind", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile","-","--workers","4"]
