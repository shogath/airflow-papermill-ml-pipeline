# Airflow Papermill ML pipeline
## Build
First make sure that these folders exist:

```
./dags
./logs
./plugins
./results
./notebooks
```

Use this command to create them:

`mkdir ./dags ./logs ./plugins ./results ./notebooks`

Edit `AIRFLOW_UID` in `.env` file with your user id.

To check your user id run `id -u`.

After the setup run `docker compose up` to build and start the app.

The app will be available at http://127.0.0.1:8080

Default credentials:
```
username: airflow
password: airflow
```

## Cleaning up

To stop and delete containers, delete volumes with database data and downloaded images, run:

`docker compose down --volumes --rmi all`

# Overview

1. Running DAG

<img src="https://github.com/shogath/airflow_papermill_ml_pipeline/blob/main/readme_assets/dags.png" />

2. Successful run

<img src="https://github.com/shogath/airflow_papermill_ml_pipeline/blob/main/readme_assets/successful_run.png" />

3. Output files will be saved in the `results` folder

<img src="https://github.com/shogath/airflow_papermill_ml_pipeline/blob/main/readme_assets/output.png" />