FROM apache/airflow:2.3.4-python3.8
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
COPY requirements.txt .
COPY .env .
COPY data ./data/
RUN pip install --no-cache-dir -r requirements.txt