from dagster import job, op
import subprocess

@op
def scrape_telegram_data():
    subprocess.run(["python", "src/telegram_scraper.py"], check=True)

@op
def load_raw_to_postgres():
    subprocess.run(["python", "src/load_to_postgres.py"], check=True)

@op
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "telegram_dbt"], check=True)

@op
def run_yolo_enrichment():
    subprocess.run(["python", "src/image_processing/detect_objects.py"], check=True)

@job
def telegram_pipeline_job():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()
